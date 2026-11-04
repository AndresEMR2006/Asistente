from core.CommandProccesor import CommandProccesor
from ai.AIengine import AIengine

ai_engine = AIengine()
procesador = CommandProccesor(ai_engine);

print(procesador.process_command("Destruye el mundo"))