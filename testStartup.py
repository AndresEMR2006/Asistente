print("INICIANDO PRUEBA")

from integrations.windows.StartupManager import StartupManager

print("IMPORTACIÓN CORRECTA")

startup = StartupManager()

print("OBJETO CREADO")

print("Habilitado:", startup.is_enabled())

startup.enable()

print("Habilitado:", startup.is_enabled())

startup.disable()

print("Habilitado:", startup.is_enabled())

input("Presiona ENTER para salir...")