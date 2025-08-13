import requests
from os import getenv
from dotenv import load_dotenv
from nltk.chat.util import Chat, reflections


# Load environment variables
load_dotenv()


TMDB_GENRE_IDS = {
    "action": 28,
    "adventure": 12,
    "animation": 16,
    "comedy": 35,
    "crime": 80,
    "documentary": 99,
    "drama": 18,
    "family": 10751,
    "fantasy": 14,
    "history": 36,
    "horror": 27,
    "music": 10402,
    "mystery": 9648,
    "romance": 10749,
    "science fiction": 878,
    "tv movie": 10770,
    "thriller": 53,
    "war": 10752,
    "western": 37,
}


def get_films(genres: str) -> list[str]:
    genre_list = genres.split()
    genre_ids = [
        str(TMDB_GENRE_IDS[genre]) for genre in genre_list if genre in TMDB_GENRE_IDS
    ]

    if genre_ids:
        PARAMS = {
            "api_key": getenv("TMDB_API_KEY"),
            "with_genres": ",".join(genre_ids),
            "sort_by": "vote_count.desc",
        }

        response = requests.get(url=f"{getenv('TMDB_URL')}", params=PARAMS)

        films = response.json()["results"]

        film_list = [(film["title"], film["release_date"]) for film in films]

        return film_list

    return None


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


run_chatbot()
