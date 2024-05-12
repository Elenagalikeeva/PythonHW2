from parserss import Parsers


def main():
    pars = Parsers("https://news.mail.ru", "newss.txt")
    pars.run()


if __name__ == '__main__':
    main()
