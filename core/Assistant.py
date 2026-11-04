from core.CommandProccesor import CommandProccesor
from core.ModuleManager import ModuleManager
from ai.AIengine import AIengine

class Assistant:

    def __init__(self):
        print("[ASSISTANT] Asistente inicializando. \n")

        self.running = False
        self.module_manager = ModuleManager()
        self.ai_engine = AIengine()
        self.command_proccesor = CommandProccesor(self.ai_engine)

        print("[ASSISTANT] Asistente inicializado correctamente. \n")

    def start(self):
        self.running = True
        print("[ASSISTANT] Asistente iniciado. \n")

    def process_command(self, user_input):
        command = self.command_proccesor.process_command(user_input)
        self.module_manager.manage(command)

    def run(self):
        self.running = True

        while self.running:
            user_input = input("...\n")

            if user_input == "salir":
                self.stop()
                continue

            self.procces_command(user_input)

            

    def stop(self):
        self.running = False
