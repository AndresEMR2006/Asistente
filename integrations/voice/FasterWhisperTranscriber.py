from faster_whisper import WhisperModel

from integrations.voice.SpeechToText import SpeechToText


class FasterWhisperTranscriber(SpeechToText):

    def __init__(
        self,
        model_size="base",
        device="cpu",
        compute_type="int8"
    ):

        self.model = WhisperModel(
            model_size,
            device=device,
            compute_type=compute_type
        )

    def transcribe(self, audio):

        audio = audio.flatten()

        segments, info = self.model.transcribe(
            audio,
            language="es"
        )

        transcription = " ".join(
            segment.text.strip()
            for segment in segments
        )

        return transcription.strip()