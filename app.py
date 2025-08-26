from PyQt6.QtWidgets import QApplication
import sys
from ui import Window
from chatbot import Chatbot


EXIT_COMMANDS = {"quit", "exit", "terminate", "close"}


class App:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = Window()
        self.chatbot = Chatbot()

        # event bindings
        self.window.submit_button.clicked.connect(self.chat)
        self.window.input.returnPressed.connect(self.chat)

        # apply stylesheet
        self._load_stylesheet("style.qss")

    def chat(self) -> None:
        """
        Handles user input from the GUI.
        Terminates the app if any exit command is entered.
        """
        text = self.window.input.text().strip()

        if not text:
            return

        if text.lower() in EXIT_COMMANDS:
            self.app.quit()

        # display user text
        self.window.display(text, "user")
        self.window.input.clear()

        # display chatbot response
        chatbot_response = self.chatbot.get_bot_response(text)
        self.window.display(chatbot_response, "chatbot")

    def start(self) -> None:
        """
        Launches the chatbot application.
        """
        self.window.show()
        sys.exit(self.app.exec())

    def _load_stylesheet(self, path: str) -> None:
        """
        Internal function to load the qss stylesheet for the app.
        """
        try:
            with open(path, "r") as qss_file:
                self.app.setStyleSheet(qss_file.read())
        except FileNotFoundError:
            print(f"Stylesheet '{path}' not found.")
