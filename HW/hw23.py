class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def name(self):
        return self.__name

    @property
    def old(self):
        return self.__old

    @name.setter
    def name(self, name):
        self.__name = name

    @old.setter
    def old(self, old):
        self.__old = old

    @name.deleter
    def name(self):
        print("Удаление свойства")
        del self.__name

    @old.deleter
    def old(self):
        print("Удаление свойства")
        del self.__old


p = Person("Irina", "26")
p.name = "Igor"
print(p.name)
p.old = "31"
print(p.old)
