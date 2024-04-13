class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pro(self):
        print("Произведение:", self.a * self.b)

    def summ(self):
        print("Сумма:", self.a + self.b)

    def change(self):
        self.a = 10
        self.b = 20


class Rtriangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def gip(self):
        print(f"Гипотенуза АВС:", round((self.a ** 2 + self.b ** 2) ** (1 / 2), 2))

    def pl(self):
        print("Площадь АВС:", self.a * 1 / 2 * self.b)

    def info(self):
        self.gip()
        print("Прямоугольный треугольник АВС (5, 8, 9.43)")
        self.pl()


p = Pair(5, 8)
r = Rtriangle(5, 8)
r.info()
print()
p.summ()
p.pro()
print()
p.change()
r.change()
r.gip()
p.summ()
p.pro()
r.pl()
