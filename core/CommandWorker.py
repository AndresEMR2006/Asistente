from PySide6.QtCore import QObject, Signal, Slot

class CommandWorker(QObject):

    command_finished = Signal()
    command_failed = Signal(str)

    def __init__(self, assistant):
        super().__init__()

        self.assistant = assistant

    @Slot(str)
    def execute(self, text):

        try:
            self.assistant.process_command(text)

        except Exception as error:
            self.command_failed.emit(str(error))

        finally:
            self.command_finished.emit()