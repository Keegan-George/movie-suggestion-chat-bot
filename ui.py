from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QWidget,
    QTextEdit,
    QLineEdit,
    QPushButton,
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 500)
        self.setWindowTitle("Movie Suggestion Chat Bot")

        # widgets
        self.chat = QTextEdit(self)
        self.chat.setReadOnly(True)
        self.input = QLineEdit(self)
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.submit)

        # layout
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.chat, 0, 0, 1, 2)
        layout.addWidget(self.input, 1, 0)
        layout.addWidget(self.submit_button, 1, 1)

    def submit(self):
        """
        Displays in the window the text entered in the line edit box.
        """
        pass


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
