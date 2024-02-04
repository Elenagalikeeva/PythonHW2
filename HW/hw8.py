def pl(p):
    if p == 1:
        a = int(input("Длина = "))
        b = int(input("Ширина = "))
        print("Площадь =", a*b)
    elif p == 2:
        o = int(input("Основание = "))
        v = int(input("Высота = "))
        print("Площадь = ", 0.5*o*v)
    elif p == 3:
        r = int(input("Радиус = "))
        print("Площадь = ", 3.14*r**2)
    else:
        print("Неверное значение")

print(pl(int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))))

