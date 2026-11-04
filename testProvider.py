from ai.providers.OllamaProvider import OllamaProvider

provider = OllamaProvider()

response = provider.generate_response("Hola, ¿cómo estás?")
print(response)