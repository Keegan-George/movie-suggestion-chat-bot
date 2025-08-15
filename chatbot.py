from nltk.chat.util import Chat, reflections
from films import get_films


class Chatbot:
    def __init__(self):
        self.pairs = [
            (r"Hello|Hi|Hey", ("Hi! How can I help you?",)),
            (
                r"Who are you?|What's your name?",
                (
                    "I'm the movie recommendation bot. I'll recommend movies based on genre.",
                ),
            ),
        ]

        self.chatbot = Chat(self.pairs, reflections)

    def get_bot_response(self, user_input):
        """
        Generates the chatbot responses.
        """

        if user_input == "quit":
            return "Bot: Goodbye."

        response = self.chatbot.respond(user_input)

        if response:
            return response

        else:
            films = get_films(user_input)
            return (
                films if films else "Bot: Sorry, I didn't get that. Please try again."
            )
