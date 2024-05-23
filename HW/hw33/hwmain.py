from parserss import Parsers
import csv


def main():
    pars = Parsers("https://news.mail.ru", "newss.csv")
    pars.run()


if __name__ == '__main__':
    main()
