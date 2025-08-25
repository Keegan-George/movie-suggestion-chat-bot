from nltk.chat.util import Chat, reflections
from films import get_films


class Chatbot:
    """
    Simple movie recommendation bot using NLTK's pattern-based chat engine.
    Responds to greetings and identity questions, and recommends films based on genre input.
    """

    def __init__(self) -> None:
        self.pairs = [
            (r"\b(hello|hi|hey)\b", ("Hi! How can I help you?",)),
            (
                r"\b((who|what) are you|what('?s|is) your name)",
                (
                    "Hey there! I'm your movie recommendation bot! Just tell me a genre(s), and I'll give you some great film suggestions.",
                ),
            ),
        ]

        self.chatbot = Chat(self.pairs, reflections)

    def get_bot_response(self, user_input: str) -> str:
        """
        Processes user input and returns an appropriate response.
        """
        user_input = user_input.strip()
        response = self.chatbot.respond(user_input)

        if response:
            return response

        films = get_films(user_input)
        return films if films else "Sorry, I didn't get that. Please try again."
