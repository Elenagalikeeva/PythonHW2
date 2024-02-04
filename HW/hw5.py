a = []
c = int(input("Кол-во элементов списка: "))

for i in range(c):
    b = int(input("Введите число кратное 3: "))
    if b % 3 == 0:
        a.append(b)
    else:
        print(b, "не делится на 3 без остатка.")
print(a)