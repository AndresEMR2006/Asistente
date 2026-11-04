import sounddevice as sd

import numpy as np

import threading

class AudioCapture:

    def __init__(self, sample_rate=16000, channels=1, dtype="float32"):

        self.sample_rate = sample_rate
        self.channels = channels
        self.dtype = dtype

        self.audio_data = []
        self.stream = None

        self.recording = False
        self.lock = threading.Lock()

    def get_devices(self):
        return sd.query_devices()

    def start_recording(self):

        with self.lock:

            if self.recording:
                raise RuntimeError("Ya existe una grabación activa.")

            self.audio_data = []
            self.recording = True

            try:
                self.stream = sd.InputStream(
                    samplerate=self.sample_rate,
                    channels=self.channels,
                    dtype=self.dtype,
                    callback=self._audio_callback
                )

                self.stream.start()

            except Exception:
                self.recording = False
                self.stream = None
                raise

    def stop_recording(self):

        with self.lock:

            if not self.recording:
                raise RuntimeError("No existe una grabación activa.")

            self.recording = False
            stream = self.stream
            self.stream = None

        stream.stop()
        stream.close()

        with self.lock:
            audio = np.concatenate(self.audio_data, axis=0)
            self.audio_data = []

        return audio

    def _audio_callback(self, indata, frames, time, status):

        if status:
            print(f"[AUDIO] {status}")

        with self.lock:

            if self.recording:
                self.audio_data.append(indata.copy())
