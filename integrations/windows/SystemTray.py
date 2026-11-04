from pathlib import Path

from PySide6.QtWidgets import (QSystemTrayIcon, QMenu, QApplication)

from PySide6.QtGui import QIcon

from integrations.windows.StartupManager import StartupManager

class SystemTray:

    def __init__(self, assistant, app):

        self.startup_manager = StartupManager()
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

        status_action = menu.addAction("Kusare está ejecutándose")
        status_action.setEnabled(False)

        menu.addSeparator()

        notification_action = menu.addAction("Acerca de Kusare")
        notification_action.triggered.connect(self.show_about)

        menu.addSeparator()

        startup_action = menu.addAction("Iniciar con Windows")
        startup_action.setCheckable(True)

        startup_action.setChecked(
            self.startup_manager.is_enabled()
        )

        startup_action.triggered.connect(
            self.toggle_startup
        )

        menu.addSeparator()

        exit_action = menu.addAction("Salir")
        exit_action.triggered.connect(self.exit_application)

        self.tray.setContextMenu(menu)

    def toggle_startup(self, checked):

        if checked:
            self.startup_manager.enable()
            print("[SYSTEM TRAY] Inicio automático habilitado.")

        else:
            self.startup_manager.disable()
            print("[SYSTEM TRAY] Inicio automático deshabilitado.")

    def show_about(self):

        self.tray.showMessage(
            "Kusare",
            "Tu asistente virtual está ejecutándose.",
            QSystemTrayIcon.MessageIcon.Information,
            3000
        )

    def exit_application(self):

        print("[SYSTEM TRAY] Cerrando Kusare...")

        self.tray.hide()
        self.app.quit()