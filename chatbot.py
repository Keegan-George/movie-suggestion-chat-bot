from nltk.chat.util import Chat, reflections
from films import get_films


class Chatbot:
    def __init__(self):
        self.pairs = [
            (r"Hello|Hi|Hey", ("Hi! How can I help you today?",)),
            (
                r"Who are you?|What's your name?",
                (
                    "I'm the movie recommendation bot. I'll recommend movies based on genre.",
                ),
            ),
        ]

        self.chatbot = Chat(self.pairs, reflections)

    def run_chatbot(self):
        """
        Type 'quit' to exit.

        """
        while True:
            user_input = input("User: ")

            if user_input == "quit":
                print("Bot: Goodbye")
                break

            response = self.chatbot.respond(user_input)

            if response:
                print(response)

            else:
                films = get_films(user_input)
                print(
                    films
                    if films
                    else "Bot: Sorry, I didn't get that. Please try again."
                )
