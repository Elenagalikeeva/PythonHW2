from math import *
print("Выберите фигуру: ")
print("1- треугольник")
print("2- прямоугольник")
print("3- круг")
f = int(input(": "))
if f == 1:
    a = int(input("Введите сторону a = "))
    b = int(input("Введите сторону b = "))
    c = int(input("Введите сторону c = "))
    p = (a + b + c) / 2
    print("Площадь равна:", sqrt(p*(p-a)*(p-b)*(p-c)))
elif f == 2:
    a = int(input("Введите сторону a = "))
    b = int(input("Введите сторону b = "))
    print("Площадь равна:", a*b)
elif f == 3:
    r = int(input("Введите радиус r = "))
    print("Площадь равна:", pi*r**2 )