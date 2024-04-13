class Student:
    def __init__(self):
        self.name1 = "Roman"
        self.name2 = "Vladimir"
        self.im = self.Inform()

    def info(self):
        print(f"{self.name1} => {self.im.mod}, {self.im.proc}, {self.im.pam}")
        print(f"{self.name2} => {self.im.mod}, {self.im.proc}, {self.im.pam}")

    class Inform:
        def __init__(self):
            self.mod = "HP"
            self.proc = "i7"
            self.pam = 16



s = Student()
s.info()
