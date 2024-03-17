class Avto:
    def __init__(self, name, year, brand, force, color, price):
        self.name = name
        self.year = year
        self.brand = brand
        self.force = force
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.name}\nГод выпуска: {self.year}\nПроизводитель: "
              f"{self.brand}\nМощность двигателя: {self.force}\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_force(self, force):
        self.force = force

    def get_force(self):
        return self.force

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


a1 = Avto("X7 М501", "2021", "BMW", "530 л.с.", "white", "10790000")
a1.print_info()
a1.set_name("X7 М501")
print(a1.get_name())
a1.set_year("2021")
print(a1.get_year())
a1.set_brand("BMW")
print(a1.get_brand())
a1.set_force("530 л.с.")
print(a1.get_force())
a1.set_color("white")
print(a1.get_color())
a1.set_price("10790000")
print(a1.get_price())
