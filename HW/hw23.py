class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def _check_value(a):
        if isinstance(a, int) or isinstance(a, str):
            return True
        return False


    @property
    def name(self):
        return self.__name

    @property
    def old(self):
        return self.__old

    @name.setter
    def name(self, name):
        if Person._check_value(name):
            self.__name = name


    @old.setter
    def old(self, old):
        if Person._check_value(old):
            self.__old = old

    @name.deleter
    def name(self):
        del self.__name

    @old.deleter
    def old(self):
        del self.__old


p = Person("Irina", 26)
print(p.__dict__)
p.name = "Igor"
print(p.name)
p.old = "31"
print(p.old)
del p.name
print(p.__dict__)
