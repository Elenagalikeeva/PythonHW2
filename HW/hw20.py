def minus_num(num):
    count = 0
    if not num:
        return 0
    if num[0] < 0:
        count += 1
    return minus_num(num[1:]) + count


a = [-2, 3, 8, -11, -4, 6]
print(minus_num(a))
