import sys

from PySide6.QtWidgets import QApplication

from core.Assistant import Assistant
from core.InteractionManager import InteractionManager

from integrations.windows.SystemTray import SystemTray
from integrations.windows.GlobalShortcuts import GlobalShortcuts
from integrations.voice.PushToTalk import PushToTalk
from integrations.voice.FasterWhisperTranscriber import FasterWhisperTranscriber

from interfaces.text.TextInput import TextInput


def main():

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    # Inicialización del núcleo
    assistant = Assistant()
    assistant.start()

    # Inicialización de interacciones
    interaction_manager = InteractionManager(assistant)

    # Inicialización de reconocimiento de voz
    transcriber = FasterWhisperTranscriber()

    push_to_talk = PushToTalk(
        transcriber=transcriber,
        on_transcription=interaction_manager.process_text
    )

    # Inicialización de interfaces
    text_input = TextInput(interaction_manager)
    interaction_manager.open_text_input.connect(text_input.open)

    # Inicialización de integraciones
    tray = SystemTray(assistant, app)

    shortcuts = GlobalShortcuts(
        on_text_input=interaction_manager.request_text_input,
        on_voice_press=push_to_talk.start_recording,
        on_voice_release=push_to_talk.stop_recording
    )

    shortcuts.start()

    # Gestión del cierre
    app.aboutToQuit.connect(shortcuts.stop)
    app.aboutToQuit.connect(interaction_manager.stop)
    app.aboutToQuit.connect(assistant.stop)

    print("[KUSARE] Aplicación iniciada correctamente.")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()