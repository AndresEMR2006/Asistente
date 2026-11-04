
import threading

from integrations.voice.AudioCapture import AudioCapture
from integrations.voice.SpeechToText import SpeechToText

class PushToTalk:

    def __init__(
        self,
        transcriber: SpeechToText,
        on_transcription,
        on_error=None
    ):

        self.audio_capture = AudioCapture()
        self.transcriber = transcriber

        self.on_transcription = on_transcription
        self.on_error = on_error

        self.recording = False
        self.processing = False

        self.lock = threading.Lock()
        self.worker = None

    def start_recording(self):

        with self.lock:

            if self.recording or self.processing:
                return False

            try:
                self.audio_capture.start_recording()
                self.recording = True

                return True

            except Exception as error:
                self._report_error(error)
                return False

    def stop_recording(self):

        with self.lock:

            if not self.recording:
                return False

            self.recording = False

            try:
                audio = self.audio_capture.stop_recording()

            except Exception as error:
                self._report_error(error)
                return False

            self.processing = True

            self.worker = threading.Thread(
                target=self._process_audio,
                args=(audio,),
                daemon=True
            )

            self.worker.start()

            return True

    def _process_audio(self, audio):

        try:

            transcription = self.transcriber.transcribe(audio)

            if transcription:
                self.on_transcription(transcription)

        except Exception as error:
            self._report_error(error)

        finally:

            with self.lock:
                self.processing = False

    def _report_error(self, error):

        if self.on_error is not None:
            self.on_error(error)
        else:
            print(f"[VOICE ERROR] {error}")
