import sys

from PySide6.QtWidgets import QApplication

from core.Assistant import Assistant
from integrations.windows.SystemTray import SystemTray

def main():
    app = QApplication(sys.argv)

    # Evitar que Qt cierre la aplicación al no tener ventanas.
    app.setQuitOnLastWindowClosed(False)

    # Inicializar el asistente.
    assistant = Assistant()
    assistant.start()

    # Inicializar la bandeja.
    tray = SystemTray(assistant, app)

    # Garantizar el cierre del asistente.
    app.aboutToQuit.connect(assistant.stop)

    print("[KUSARE] Aplicación iniciada correctamente.")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()