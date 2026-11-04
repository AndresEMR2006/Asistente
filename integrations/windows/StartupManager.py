import winreg
from pathlib import Path


class StartupManager:

    REGISTRY_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"
    APP_NAME = "Kusare"

    def __init__(self):

        self.executable = Path(__file__).resolve().parents[2] / ".venv" / "Scripts" / "pythonw.exe"
        self.main_file = Path(__file__).resolve().parents[2] / "Main.py"

    def enable(self):

        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            self.REGISTRY_PATH,
            0,
            winreg.KEY_SET_VALUE
        ) as key:

            command = f'"{self.executable}" "{self.main_file}"'

            winreg.SetValueEx(
                key,
                self.APP_NAME,
                0,
                winreg.REG_SZ,
                command
            )

    def disable(self):

        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            self.REGISTRY_PATH,
            0,
            winreg.KEY_SET_VALUE
        ) as key:

            try:
                winreg.DeleteValue(key, self.APP_NAME)
            except FileNotFoundError:
                pass

    def is_enabled(self):

        try:
            with winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                self.REGISTRY_PATH,
                0,
                winreg.KEY_READ
            ) as key:

                winreg.QueryValueEx(key, self.APP_NAME)
                return True

        except FileNotFoundError:
            return False