from abc import ABC, abstractmethod
import numpy as np


class SpeechToText(ABC):

    @abstractmethod
    def transcribe(self, audio: np.ndarray) -> str:
        pass