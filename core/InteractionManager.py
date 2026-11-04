from PySide6.QtCore import QObject, Signal, QThread

from core.CommandWorker import CommandWorker


class InteractionManager(QObject):

    open_text_input = Signal()
    toggle_voice = Signal()

    command_requested = Signal(str)

    def __init__(self, assistant):
        super().__init__()

        self.assistant = assistant

        # Crear hilo
        self.thread = QThread()

        # Crear trabajador
        self.worker = CommandWorker(assistant)

        # Mover trabajador al hilo secundario
        self.worker.moveToThread(self.thread)

        # Conectar solicitud de comandos
        self.command_requested.connect(self.worker.execute)

        # Iniciar hilo
        self.thread.start()

        # Conectar resultados
        self.worker.command_finished.connect(
            self.on_command_finished
        )

        self.worker.command_failed.connect(
            self.on_command_failed
        )

        print("[INTERACTION] Gestor de interacciones inicializado.")

    def request_text_input(self):
        self.open_text_input.emit()

    def request_voice_toggle(self):
        self.toggle_voice.emit()

    def process_text(self, text):

        if not text.strip():
            return

        self.command_requested.emit(text)

    def on_command_finished(self):
        print("[INTERACTION] Procesamiento finalizado.")

    def on_command_failed(self, error):
        print(f"[INTERACTION] Error procesando comando: {error}")

    def stop(self):

        self.thread.quit()
        self.thread.wait()

        print("[INTERACTION] Hilo de procesamiento detenido.")