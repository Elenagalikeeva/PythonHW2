from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, a, b, c, color):
        self.a = a
        self.b = b
        self.c = c
        self.color = color

    @abstractmethod
    def perim(self):
        pass

    @abstractmethod
    def plo(self):
        pass

    @abstractmethod
    def ris(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def perim(self):
        return self.a * 4

    def plo(self):
        return self.a ** 2

    def ris(self):
        for i in range(self.a):
            print(self.a * "*")

    def info(self):
        print("===Квадрат===")
        print("Сторона:", self.a)
        print("Цвет:", self.color)
        print("Периметр:", self.perim())
        print("Площадь:", self.plo())
        self.ris()


class Rectangle(Shape):
    def perim(self):
        return (self.a + self.b) * 2

    def plo(self):
        return self.a * self.b

    def ris(self):
        for i in range(self.a):
            print(self.b * "*")

    def info(self):
        print("===Прямоугольник===")
        print("Длина:", self.a)
        print("Ширина:", self.b)
        print("Цвет:", self.color)
        print("Периметр:", self.perim())
        print("Площадь:", self.plo())
        self.ris()


class Triangle(Shape):
    def perim(self):
        return self.a + self.b + self.c

    def plo(self):
        return round((self.perim() / 2 * (self.perim() / 2 - self.a) * (self.perim() / 2 - self.b) *
                      (self.perim() / 2 - self.c)) ** (1 / 2), 2)

        def ris(self):
            while i >= 1:


            # for i in range(self.b):
            #     print(self.b * "*")

    def info(self):
        print("===Треугольник===")
        print("Сторона 1:", self.a)
        print("Сторона 2:", self.b)
        print("Сторона 3:", self.c)
        print("Цвет:", self.color)
        print("Периметр:", self.perim())
        print("Площадь:", self.plo())
        self.ris()


s = Square(3, b=None, c=None, color="red")
r = Rectangle(3, 7, c=None, color="green")
t = Triangle(11, 6, 6, "yellow")

s.info()
print()
r.info()
print()
t.info()
