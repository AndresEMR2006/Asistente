from ai.providers.OllamaProvider import OllamaProvider

class AIengine:

    def __init__(self):
        self.provider = OllamaProvider()

        print("[AI ENGINE] Motor de IA inicializado correctamente")

    def generate_response(self, user_prompt, system_prompt):
        return self.provider.generate_response(user_prompt, system_prompt)