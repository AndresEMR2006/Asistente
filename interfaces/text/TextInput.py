
from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)


class TextInput(QWidget):

    def __init__(self, interaction_manager):
        super().__init__()

        self.interaction_manager = interaction_manager

        # Configuración de la ventana
        self.setWindowTitle("Kusare")
        self.setFixedSize(350, 100)

        # Componentes
        self.input = QLineEdit()
        self.input.setPlaceholderText("Escribe una instrucción...")

        self.send_button = QPushButton("Enviar")

        # Distribución
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

        # Eventos
        self.send_button.clicked.connect(self.send_message)
        self.input.returnPressed.connect(self.send_message)

    def send_message(self):

        text = self.input.text().strip()

        if not text:
            return

        self.interaction_manager.process_text(text)

        self.input.clear()
        self.hide()

    def open(self):

        self.show()
        self.activateWindow()
        self.input.setFocus()
