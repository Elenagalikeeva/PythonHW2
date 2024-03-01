def decor(func):
    def res(c,d):
        average = c/d
        func(c,d)
    return res

@decor
def su(*args):
    a = sum(args)
    b =
    return a, b



su(2, 3, 3, 4)