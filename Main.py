import sys

from PySide6.QtWidgets import QApplication

from core.Assistant import Assistant
from core.InteractionManager import InteractionManager

from integrations.windows.SystemTray import SystemTray
from integrations.windows.GlobalShortcuts import GlobalShortcuts

from interfaces.text.TextInput import TextInput

def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    assistant = Assistant()
    assistant.start()

    tray = SystemTray(assistant, app)

    interaction_manager = InteractionManager(assistant)

    text_input = TextInput(interaction_manager)

    interaction_manager.open_text_input.connect(text_input.open)

    shortcuts = GlobalShortcuts(
        on_text_input=interaction_manager.request_text_input,
        on_voice_toggle=interaction_manager.request_voice_toggle
    )

    shortcuts.start()

    app.aboutToQuit.connect(assistant.stop)
    app.aboutToQuit.connect(interaction_manager.stop)

    print("[KUSARE] Aplicación iniciada correctamente.")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()