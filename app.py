from PyQt6.QtWidgets import QApplication
import sys
from ui import Window
from chatbot import Chatbot


class App:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = Window()
        self.chatbot = Chatbot()

        # events
        self.window.submit_button.clicked.connect(self.chat)
        self.window.input.returnPressed.connect(self.chat)

        # apply stylesheet
        with open("style.qss", "r") as qss_file:
            _style = qss_file.read()
            self.app.setStyleSheet(_style)

    def chat(self) -> None:
        """
        Submits question to the chatbot.
        """
        text = self.window.input.text()

        if text.lower() in ("quit", "exit"):
            self.app.quit()

        if text:
            self.window.display(text, "user")
            self.window.input.clear()

            chatbot_response = self.chatbot.get_bot_response(text)

            self.window.display(chatbot_response, "chatbot")

    def start(self) -> None:
        self.window.show()
        sys.exit(self.app.exec())
