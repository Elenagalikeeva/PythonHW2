from bs4 import BeautifulSoup
import requests
import csv


class Parsers:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find_all("div", class_="cols__inner")
        for y in news:
            chapter = y.find("span", class_="hdr__inner")
            href = y.find("a").get("href")
            title = y.find("span", "newsitem__text")
            self.res.append({
                "chapter": chapter,
                "href": href,
                "title": title
            })

    def save(self):
        with open(self.path, "w") as f:
            writer = csv.writer(f, delimiter=";", lineterminator="\r")
            writer.writerow(["Раздел: ", "Ссылка", "Название"])
            x = 1
            for i in self.res:
                writer.writerow(["['chapter']",['href']}\n"
                                f"Название: {i['title']}\n\n{'*' * 40}\n")
                x += 1

    # f"Новость № {x}\n\nРаздел: {i['chapter']}\n"
    # f"Ссылка: {i['href']}\n"
    # f"Название: {i['title']}\n\n{'*' * 40}\n")
    # x += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
