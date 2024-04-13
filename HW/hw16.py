def decor(func):
    def res(*ars):
        print("Среднее арифметическое чисел = ", func(*ars) / len(ars))
    return res


@decor
def su(*args):
    print("Сумма чисел = ", sum(args))
    return sum(args)


su(1, 2, 3, 4)
