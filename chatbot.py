from nltk.chat.util import Chat, reflections
from films import get_films


pairs = [
    (r"Hello|Hi|Hey", ("Hi! How can I help you today?",)),
    (
        r"Who are you?|What's your name?",
        ("I'm the movie recommendation bot. I'll recommend movies based on genre.",),
    ),
]


chatbot = Chat(pairs, reflections)


def run_chatbot():
    """
    Type 'quit' to exit.

    """
    while True:
        user_input = input("User: ")

        if user_input == "exit":
            print("Bot: Goodbye")
            break

        response = chatbot.respond(user_input)

        if response:
            print(response)

        else:
            films = get_films(user_input)
            print(
                films if films else "Bot: Sorry, I didn't get that. Can you try again."
            )
