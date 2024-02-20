# s= 0
#
# def outer(a, b, c):
#     def inner(i, k):
#         return i*k
#
#     global s
#     s = 2 * (inner(a, b)+inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))


# 2


def outer(a, b, c):
    s = 0

    def inner(i, k):
        nonlocal s
        s += i * k

    inner(a, b)
    inner(a, c)
    inner(b, c)
    return 2 * s


print(outer(2, 4, 6))
print(outer(5, 8, 2))
