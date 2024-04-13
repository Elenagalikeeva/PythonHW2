class Pl:
     def __init__(self, a, b, c, d, r, v):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.r = r
        self.v = v

    @staticmethod
    def tre(a, b):
        return a * b / 2


    @staticmethod
    def ocr(r):
        return r ** 2 * 3.14

    @staticmethod
    def cvad(v):
        return v ** 2

    @staticmethod
    def pr(c, d):
        return c * d

    # @staticmethod
# def colvo():



p = Pl(6, 7, 3, 7, 3, 7)
print("Площадь треугольника через основание и высоту (6,7): ", Pl.tre(6, 7))
print("Площадь окружности: ", Pl.ocr(5))
print("Площадь квадрата (7): ", Pl.cvad(7))
print("Площадь прямоугольника(3,7): ", Pl.pr(3, 7))
print("Количество подсчетов площади: ", )
