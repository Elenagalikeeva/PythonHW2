a = int(input("Введите число от 1 до 99:"))
b = a % 10
if 1 <= a <= 10 or 15 <= a <= 99:
    if 2 <= b <= 4:
        print(a, "копейки")
    if b == 1:
        print(a, "копейка")
    if 5 <= b <= 9 or b == 0:
        print(a, "копеек")
if 11 <= a <= 14:
    print(a, "копеек")
if 0 >= a or a >= 100:
    print("не верное значение")