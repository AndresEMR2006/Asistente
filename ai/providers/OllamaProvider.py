import ollama

COMMAND_SCHEMA = {
    "type": "object",
    "properties": {
        "module": {
            "type": ["string", "null"]
        },
        "action": {
            "type": ["string", "null"]
        },
        "parameters": {
            "type": "object",
            "additionalProperties": True
        }
    },
    "required": [
        "module",
        "action",
        "parameters"
    ]
}

class OllamaProvider:

    def __init__(self, model="qwen2.5:3b"):

        self.model = model

        print("[OLLAMA] Proveedor de IA Ollama inicializado correctamente")

    def generate_response(self, user_prompt, system_prompt):

        response = ollama.chat(
            model = self.model,
            messages = [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            format = COMMAND_SCHEMA
        )
        return response.message.content