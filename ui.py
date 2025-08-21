from PyQt6.QtWidgets import (
    QGridLayout,
    QWidget,
    QLineEdit,
    QPushButton,
    QListWidget,
    QListWidgetItem,
)

from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(400, 500)
        self.setWindowTitle("Movie Suggestion Chat Bot")

        # widgets
        self.chat = QListWidget(self)
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

        chat_bubble = QListWidgetItem(text)

        if sender == "user":
            chat_bubble.setTextAlignment(Qt.AlignmentFlag.AlignLeft)

        elif sender == "chatbot":
            chat_bubble.setTextAlignment(Qt.AlignmentFlag.AlignRight)

        self.chat.addItem(chat_bubble)
