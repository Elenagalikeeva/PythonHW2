def minus_num(num):
    count = 0
    for i in num:
        if i < 0:
            count += 1
        else:
            minus_num(num)
    return count


a = [-2, 3, 8, -11, -4, 6]
print(minus_num(a))
