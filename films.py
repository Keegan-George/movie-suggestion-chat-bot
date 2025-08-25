import string
import requests
from os import getenv
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

TMDB_URL = getenv("TMDB_URL")
TMDB_API_KEY = getenv("TMDB_API_KEY")

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


def get_films(phrase: str) -> str:
    """
    Extract movie genres from a phrase and return a list of recommended films using the TMDB API.
    Return None if no valid genres are found
    """
    # extract TMDB genre IDs
    genre_ids = extract_genre_ids(phrase)

    # return list of films from TMBD API
    if genre_ids:
        PARAMS = {
            "api_key": TMDB_API_KEY,
            "with_genres": ",".join(genre_ids),
            "sort_by": "vote_count.desc",
        }

        response = requests.get(url=TMDB_URL, params=PARAMS)

        films = response.json()["results"]

        film_list = [
            f"{index}. {film['title']}, {film['release_date']}"
            for index, film in enumerate(films, start=1)
        ]

        films_string = "\n".join(film_list)

        return films_string

    return None


def extract_genre_ids(phrase: str) -> list[str]:
    """
    Extract TMBD genre IDs from a phrase.
    """
    cleaned_phrase = phrase.translate(str.maketrans("", "", string.punctuation))
    words = cleaned_phrase.lower().split()
    return [str(TMDB_GENRE_IDS[genre]) for genre in words if genre in TMDB_GENRE_IDS]
