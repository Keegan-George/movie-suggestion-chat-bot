from PyQt6.QtWidgets import (
    QGridLayout,
    QWidget,
    QLineEdit,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QLabel,
    QHBoxLayout,
)


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

        # label to serve as the chat bubble
        chat_bubble = QLabel(text)
        chat_bubble.setWordWrap(True)

        # create a layout for the bubble
        bubble_layout = QHBoxLayout()

        # add bubble to layout and position left/right accordingly
        if sender == "user":
            bubble_layout.addWidget(chat_bubble)
            bubble_layout.addStretch()
            chat_bubble.setObjectName("userBubble")

        elif sender == "chatbot":
            bubble_layout.addStretch()
            bubble_layout.addWidget(chat_bubble)
            chat_bubble.setObjectName("chatbotBubble")

        # create a container and apply layout
        bubble_container = QWidget()
        bubble_container.setLayout(bubble_layout)

        # add to list and set to container
        item = QListWidgetItem()
        item.setSizeHint(bubble_container.sizeHint())
        self.chat.addItem(item)
        self.chat.setItemWidget(item, bubble_container)
