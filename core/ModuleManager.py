from modules.youtube.Youtube import Youtube
from modules.windows.Windows import Windows

import json

class ModuleManager:

    def __init__(self):
        self.modules = {}

        

        print()
        # Aqui iran las funciones para crear los modulos
        self.modules['youtube'] = Youtube()
        self.modules['windows'] = Windows()

        print("\n[MODULES] Gestor de módulos inicializado. \n")

    def manage(self, input):

        module = input["module"]
        action = input["action"]
        parameters = input["parameters"]

        # print(input)
        # print(module)
        # print(action)
        print(parameters)

        match(module):
            case "windows":
                match (action):
                    case "abrir":
                        application = parameters["app"]
                        self.modules['windows'].open_application(application)
            case "youtube":
                print("Aun no implementado")
            case "base":
                print("Aun no implementado")
            case "error":
                print("Aun no implementado")
