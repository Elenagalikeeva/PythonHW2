class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec % other.sec)

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec < other.sec:
            return True
        return False

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec <= other.sec:
            return True
        return False

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec > other.sec:
            return True
        return False

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        if self.sec >= other.sec:
            return True
        return False

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == "hour":
            return (self.sec // 3600) % 24
        elif item == "min":
            return (self.sec // 60) % 60
        elif item == "sec":
            return self.sec % 60
        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")

        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом")

        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24

        if key == "hour":
            self.sec = s + 60 * m + value * 3600
        if key == "min":
            self.sec = s + 60 * value + h * 3600
        if key == "sec":
            self.sec = value + 60 * m + h * 3600


c1 = Clock(100)
c2 = Clock(200)
c4 = Clock(300)
print(c1.get_format_time())
print(c2.get_format_time())
print(c4.get_format_time())
c3 = c2 - c1
print(c3.get_format_time())
c3 = c2 *c1
print(c3.get_format_time())
c3 = c2 // c1
print(c3.get_format_time())
c3 = c2 % c1
print(c3.get_format_time())
print()
if c1 < c2:
    print("Время c1 меньше c2")
else:
    print("Время c1 больше c2")

if c1 <= c2:
    print("Время c1 меньше либо равно c2")
else:
    print("Время c1 больше c2")

if c1 > c2:
    print("Время c1 больше  c2")
else:
    print("Время c1 меньше c2")

if c1 >= c2:
    print("Время c1 больше либо равно c2")
else:
    print("Время c1 меньше c2")


