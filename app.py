from PyQt6.QtWidgets import QApplication
import sys
from ui import Window
from chatbot import Chatbot


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = Window()
        self.chatbot = Chatbot()

        # events
        self.window.submit_button.clicked.connect(self.chat)
        self.window.input.returnPressed.connect(self.chat)

    def chat(self):
        """
        Submits question to the chatbot.
        """
        text = self.window.input.text()

        if text == "quit":
            self.app.quit()

        if text:
            self.window.display(text)
            self.window.input.clear()

            chatbot_response = self.chatbot.get_bot_response(text)

            self.window.display(chatbot_response)

    def start(self):
        self.window.show()
        sys.exit(self.app.exec())
