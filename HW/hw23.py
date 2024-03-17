class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old


    @property
    def name(self):
        return self.__name, self.__old

    @name.setter
    def name(self, name, old):
        self.__name = name
        self.__old = old

    @name.deleter
    def name(self):
        print("Удаление свойства")
        del self.__name
        del self.__old


p = Person("Irina", "26")
p.name = "Igor", "31"
print(p.name)



