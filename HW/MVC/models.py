import pickle
import os.path


class Film:
    def __init__(self, title, genre, author, year, duration, studio, actors):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.author})"


class FilmModel:
    def __init__(self):
        self.film_name = "film.txt"
        self.film = self.load_data()


    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.film[film.title] = film

    def get_all_films(self):
        return self.film.values()

    def get_single_film(self, user_title):
        film = self.film[user_title]
        dict_film = {
            "название ":film.title,
            "жанр": film.genre,
            "режиссер": film.author,
            "год выпуска": film.year,
            "длительность": film.duration,
            "студия": film.studio,
            "актеры": film.actors
        }
        return dict_film

    def remove_film(self, user_title):
        return self.film.pop(user_title)

    def save_data(self):
        with open(self.film_name, "wb") as f:
            pickle.dump(self.film, f)

    def load_data(self):
        if os.path.exists(self.film_name):
            with open(self.film_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()