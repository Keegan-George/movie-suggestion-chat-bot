from PyQt6.QtWidgets import (
    QGridLayout,
    QWidget,
    QTextEdit,
    QLineEdit,
    QPushButton,
)


from PyQt6.QtGui import QTextCursor, QTextBlockFormat
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(400, 500)
        self.setWindowTitle("Movie Suggestion Chat Bot")

        # widgets
        self.chat = QTextEdit(self)
        self.chat.setReadOnly(True)
        self.input = QLineEdit(self)
        self.input.setFocus()
        self.submit_button = QPushButton("Submit", self)

        # layout
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.chat, 0, 0, 1, 2)
        layout.addWidget(self.input, 1, 0)
        layout.addWidget(self.submit_button, 1, 1)

    def display(self, text: str, sender: str) -> None:
        """
        Display text in the chat window.
        """
        cursor = self.chat.textCursor()

        block_format = QTextBlockFormat()

        if sender == "user":
            block_format.setAlignment(Qt.AlignmentFlag.AlignLeft)

        elif sender == "chatbot":
            block_format.setAlignment(Qt.AlignmentFlag.AlignRight)

        cursor.insertBlock(block_format)

        self.chat.append(text)
