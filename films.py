import requests
from os import getenv
from dotenv import load_dotenv


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
