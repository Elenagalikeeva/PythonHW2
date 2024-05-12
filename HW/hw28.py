class Valid:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} должно быть только целочисленным значением")
        instance.__dict__[self.name] = value


class Point3D:
    x = Valid()
    y = Valid()
    z = Valid()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__)

