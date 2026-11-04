import subprocess

class Windows:

    def __init__(self):
        print("[MODULE] Módulo de Windows inicializado.")
        self.applications = {
            "notas": "notepad.exe"
        }


    def open_application(self, application_name):
        if application_name in self.applications:
            app_route = self.applications.get(application_name)
            subprocess.Popen([app_route])

            print("[WINDOWS] aplicacion abierta exitosamente")
        else:
            print("[WINDOWS] la aplicacion no esta en el diccionario")