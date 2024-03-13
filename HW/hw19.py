import re
def validate(login):
    return re.findall(r"^[A-z\d\w\-?\@?]{6,18}$", login)


print(validate(input("Введите пароль: ")))