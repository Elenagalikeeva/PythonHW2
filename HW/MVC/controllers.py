from views import UserInterface
from models import FilmModel


class Controller:
    def __init__(self):
        self.article_model = FilmModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            title = self.user_interface.add_user_film()
            self.article_model.add_film(title)
        elif answer == "2":
            catalog = self.article_model.get_all_films()
            self.user_interface.show_all_films(catalog)
        elif answer == "3":
            title_view = self.user_interface.get_user_film()
            try:
                film = self.article_model.get_single_film(title_view)
            except KeyError:
                self.user_interface.show_incorrect_title_error(title_view)
            else:
                self.user_interface.show_single_film(film)
        elif answer == "4":
            title_view = self.user_interface.get_user_film()
            try:
                title = self.article_model.remove_film(title_view)
            except KeyError:
                self.user_interface.show_incorrect_title_error(title_view)
            else:
                self.user_interface.remove_single_article(title)
        elif answer == "q":
            self.article_model.save_data()
        else:
            self.user_interface.show_incorrect_answer_error(answer)