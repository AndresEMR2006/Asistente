from pathlib import Path

from PySide6.QtWidgets import (QSystemTrayIcon, QMenu, QApplication)

from PySide6.QtGui import QIcon

class SystemTray:

    def __init__(self, assistant, app):

        self.assistant = assistant
        self.app = app

        self.tray = QSystemTrayIcon()

        icon_path = Path(__file__).resolve().parents[2] /"assets"/"kusare.ico"

        if icon_path.exists():
            self.tray.setIcon(QIcon(str(icon_path)))
        else:
            self.tray.setIcon(
                self.app.style().standardIcon(
                    self.app.style().StandardPixmap.SP_ComputerIcon
                )
            )

        self.tray.setToolTip("Kusare - Asistente virtual")
        self.create_menu()
        self.tray.show()

        print("[SYSTEM TRAY] Bandeja del sistema inicializada.")


    def create_menu(self):

        menu = QMenu()

        status_action = menu.addAction("Kusare esta ejecutandose")
        status_action.setEnabled(False)

        menu.addSeparator

        notification_action = menu.addAction("Acerca de Kusare")
        notification_action.triggered.connect(self.show_about)

        menu.addSeparator()

        exit_action = menu.addAction("Salir")
        exit_action.triggered.connect(self.exit_application)

        self.tray.setContextMenu(menu)

    def show_about(self):

        self.tray.showMessage(
            "Kusare",
            "Tu asistente virtual está ejecutándose.",
            QSystemTrayIcon.MessageIcon.Information,
            3000
        )

    def exit_application(self):

        print("[SYSTEM TRAY] Cerrando Kusare...")

        self.assistant.stop()
        self.tray.hide()
        self.app.quit()