from PyQt6.QtWidgets import (
    QGridLayout,
    QWidget,
    QTextEdit,
    QLineEdit,
    QPushButton,
)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(400, 500)
        self.setWindowTitle("Movie Suggestion Chat Bot")

        # widgets
        self.chat = QTextEdit(self)
        self.chat.setReadOnly(True)
        self.chat.setAcceptRichText(True)
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

        chat_bubble = f"""
            <table width="100%" cellspacing="0" cellpadding="4">
                <tr>
                    {'<td width="60%">' if sender == 'user' else '<td width="40%"></td><td width="60%">'}
                        <div style="
                            background-color:{'#FFD580' if sender == 'user' else '#C1E1C1'};
                            border-radius: 12px;
                            font-size: 12px;
                            padding: 4px;
                            color: black;
                            font-family: Courier;
                        ">
                            {text}
                        </div>
                    </td>
                </tr>
            </table>
        """

        self.chat.insertHtml(chat_bubble)
