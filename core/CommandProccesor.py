from ai.AIengine import AIengine

import json

class CommandProccesor:

    SYSTEM_PROMPT = """
    Eres el intérprete de comandos de Kusare.

    Tu responsabilidad es interpretar las instrucciones del usuario
    y determinar qué módulo y acción deben ejecutarse.

    No debes ejecutar acciones directamente.

    REGLAS:
    - Solo puedes utilizar los módulos y acciones definidos abajo.
    - No inventes módulos, acciones ni parámetros.
    - Si una solicitud no corresponde a ninguna acción disponible,
    utiliza el módulo "error" y la acción "error".
    - si hay una sinonimo de una aplicacion utiliza el nombre definido
    en los paremetros, no el que te de el usuario

    MODULES:

    1. youtube
        actions:
        - buscar
            parameters:
            - query
        - pausar

    2. windows
        actions:
        - abrir
            parameters:
            - app
            Aplicaciones disponibles:
            - "notas"

    3. base
        actions:
        - salir

    4. error
        actions:
        - error
    """

    def __init__(self, ai_engine):
        self.ai_engine = ai_engine
        print("[COMMAND PROCCESOR] analizador de comando inizializado correctamente")

    def process_command(self, user_input):

        response = self.ai_engine.generate_response(user_input, self.SYSTEM_PROMPT)

        return json.loads(response)

