i = 0
a = int(input("Кол-во символов: "))
b = input("Тип символа: ")
print("0- горизонтальная ориентация")
print("1- вертикальная ориентация")
c = int(input("Ориентация линии: "))
while i < a:
    if c == 0:
        print(b*a)
        break
    else:
        print(b)
    i += 1

