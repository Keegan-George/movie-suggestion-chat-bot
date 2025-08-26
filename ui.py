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

USER = "user"
BOT = "chatbot"


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(400, 500)
        self.setWindowTitle("Movie Suggestion Chat Bot")

        # widgets
        self.chat = QListWidget(self)
        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Type your message here...")
        self.submit_button = QPushButton("Submit", self)

        # layout
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(self.chat, 0, 0, 1, 2)
        layout.addWidget(self.input, 1, 0)
        layout.addWidget(self.submit_button, 1, 1)

    def display(self, text: str, sender: str) -> None:
        """
        Display a chat bubble in the chat window aligned by sender.
        """
        # create chat bubble
        chat_bubble = self._create_chat_bubble(text, sender)

        # create list widget item and set height
        item = QListWidgetItem()
        item.setSizeHint(chat_bubble.sizeHint())

        # add list widget item and set to chat bubble
        self.chat.addItem(item)
        self.chat.setItemWidget(item, chat_bubble)

        # scroll chat window to the bottom
        self.chat.scrollToBottom()

    def _create_chat_bubble(self, text: str, sender: str):
        """
        Create a chat bubble aligned (left or right) based on the sender (user or chatbot accordingly).
        """
        # label acts as the chat bubble
        label = QLabel(text)
        label.setWordWrap(True)

        # create horizontal layout for the chat bubble
        layout = QHBoxLayout()

        # add label to layout and position left or right
        if sender == USER:
            layout.addWidget(label)
            layout.addStretch()
            label.setObjectName("userBubble")

        elif sender == BOT:
            layout.addStretch()
            layout.addWidget(label)
            label.setObjectName("chatbotBubble")

        # create a container for the bubble and set layout
        container = QWidget()
        container.setLayout(layout)

        return container
