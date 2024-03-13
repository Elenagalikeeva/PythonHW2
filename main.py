# print("привет")
# age = 20
# print(age)
# print(age)

# a = b = c = 5
# a, b, c = 7, 'Hello', 9.8

# PI = 3.14
# print(PI)

# num = 4321
# a = num % 10
# print(a)
# num = num // 10
# # print('num:', num)
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
# num = a * 1000 + b *100 + c *10 + d

# print(num)

# a = round(3.5768686, 2)
# print(a)
# print(round(3.8))

# name = 'vity'
# age = 20
# print('mne', name, age, "years")
# print('mne', name, age, "years", sep="---", end=" ")
# print("hello")


# name = input("name:")
# city = input("city:")
# print(name, city)

# a = int(input("1:"))
# b = int(input("2:"))
# c = int(input("3:"))
# d = int(input("4:"))
# sum1 = a + b
# sum2 = c + d
# res = sum1 / sum2
# print(round(res, 2))


# b1 = True
# b2 = False
# print(b1 + 5)  # 1
# print(b2 + 5)  # 0
#
# print(bool("py"))
# print((bool("")))
# print(bool(None))  # null


# print(2 < 4 < 9)
# print(2 < 4 > 9)  # t : f = f
# print(2==2 and 1+3==4)  # true
# print(2==2 or 1+2==4)  # true
# print( not 9-5)  # false
# print( not 9-9)  # true


# cnt = 5
# if cnt < 10:
#     cnt +=1
# print(cnt)


# age = int(input("age:"))
# if age >= 18:
#     print("yes")
# else:  # else if = elif
#     print("no")


# a = int(input("1: "))
# b = int(input("2: "))
# c = int(input("3: "))
# if a == b == c:
#     print("==")
# elif a == b or a == c or b == c:
#     print("2")
# else:
#     print("different")


# day = int(input(" day of week"))
# if (day >= 1) and (day <= 5):          # 1 <= day <= 5:
#     print("work day", end="")
#     if day ==1:
#         print("monday")
#
# elif day == 6 or day == 7:
#     print("holiday", end="")
#     if day == 6:
#         print("satarday")
# else:
#     print("no day")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# m = int(input("Введите номер месяца: "))
# if m == 1 or m == 2 or m == 12:
#     print("Зима")
# elif 3 <= m <= 5:
#     print("Весна")
# elif 6 <= m <= 8:
#     print("Лето")
# elif 9 <= m <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


# password = "admin1"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Пароль неверен")

# day = 'суббота'
# time = 18
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье' if 9 <= time <= 12:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")


# a, b = 30, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a == b" if a == b else ("a > b" if a > b else "b > a"))

# a, b = int(input("Введите первое число")), int(input("Введите второе число"))
#
# print("На ноль делить нельзя!!!" if b == 0 else a / b)

# a = 5
# b = 0
# print(a / b)


# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки и нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключений
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")


# n= input("number one:")
# m =input("number two:")
#
# try:
#     n = int(n)
#     m = int(m)
#
# except ValueError:
#     n = str(n)
# finally:
#     print(n+m)


# цикл

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1


# n = int(input("*: "))
# print("*" * n)


# n = int(input("*: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i +=1


# n = int(input("*: "))
# i = 0
# while i < n:
#      if i % 2 == 0
#          print("*", end="")
#      else:
#          print("-", end="")
#      i +=1


# a = int(input("start: "))
# b = int(input("end: "))
# res = 0
# if a > b:
#     a, b = b, a
# while a <= b:
#     if a % 2:
#         res += a
#     a +=1
# print("summa: ", res)


# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break


# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print("Результат:", res)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# j = 0
# while j < 5:
#     print(" " * j, "*", sep="")
#     j +=1


# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1


# for i in "hello":  # for element in collection
#     print(i)


# for color in "red", "orange", "green", 20, 1:  # картеж
#     print(color)


# print(range(9))
# range(start, stop, step)    range(1, 9, 2)
#
# for i in range(9):
#    print(i, end="")   0 1 2 3 4 5 6 7 8

# for i in range(9, 0, -1):
#     print(i)


# for i in range(10,100):
#     if i // 10 = i % 10:
#         print(i, end=" ")


# for i in range(3):
#     print(i)
#     if i ==1:
#         break  # прерывает else , continue нет
# else:
#     print("done")
#
#
#
# print([i * 2 for i in "Python"])  # pp yy tt ...
# print([i for i in range(30) if i %2 == 0])
#
#
#
#
#
# # Списки (list)
#
# num = [9, 3, 9, 4, 1, "hello", 2.3, true]
# print(num)
# print(type(num))
# print(num[0])  # 0
# num[1] = 100
# num[2] += 50
# print(len(num))
#
# nums = list("hello")
# num = []
# print(nums)
#
# nums = list(range(2, 100, 10))
# print(nums)
#
# for i in range(len(nums)):  # index
#     print(i)
#
#
#
# # генератор списков
# # [выражение for  переменная in последовательность]
#
# a =[0 for i in range(5)]
# print(a)  # [0,0,0,0,0]
#
# b =[i for i in range(5)]
# print(b)  # [0,1,2,3,4]
#
# c = [c *3 for c in "list"]
# print(c)  # [lll, ...]
#
# a = [0] * int(input("введите кол-во элементов списка: "))
# print(a)  # [0,0,0]
# for i  in range(len(a));
#     a[i] = int(input("->"))
# print(a)
#
#
# a = [input() for i in range(int(input("n  = ")))]
# print(a)
#
#
# s = [2, 3, 4, 5]
# for i in range(len(s)):
#     print(i, " ", s[i])
# print(len(s))
#
# a = [int(input()) for i in range(int(input("n  = ")))]
# print(a)
# s =0
# # for i in range(len(a)):
# #     if a[i]< 0:
# #         s += a[i]
# # print(s)
#
# for i in a:
#     if i < 0:
#         s += i
# print(s)
#
# lst = list(range(10, 100, 10))
# print(lst)
# for i in range(len(lst)):  # 0 1 2 3 4...
#     print(lst[i], end=" ")
# print()
# for i in lst:  # 10, 20, 30...
#     print(i, end=" ")
#
#
# n = list(range(21, 41))
# print(n)
# count = s = 0
# for i in range(len(n)):
#     if n[i]%2 == 0:
#         count += 1
#     else:
#         s += n[i]
# print("Четные: ", count)
# print("сумма: ", s)

# for i in n:
#     if i %2 ==0:
#         count +=1
#     else:
#         s +=1
# print(count, s)


# n = list(range(21, 41))
# print(n)
# i =2
# print(n[i])
# print(n[i - 1])

# a = [int(input()) for i in range(int(input("n  = ")))]
# print(a)
#
# for i in range(1, len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end=" ")
#
# a = [7, 9, 3, 1, 2]
# print(a)
#
# print(a)

# Срезы  - список[start:stop:step]
# s = [6, 9, 3, 7, 1, 8]
# print(s, id(s))
# b = s[5:16]
# print(b, id(b))
# i = 5
# while i > 0:
#     print(s[i])
#     i -= 1

# s = "Hello World!"
# print(s[6:-1])

# [1, 2, 3, 4, 5, 6, 7]
# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[-3:])
# print(s[4:1:-1])
# print(s[2:5])


# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2:5] = []
# print(s)
# del s[1:3]
# print(s)

# Методы списков
# dir(list)
# s = [9, 3, 7, 8, 4, 6, 5]
# print(s)
# # s[len(s):] = [12]
# s.append(12)  # добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет любое кол-во элементов в конец списка
# print(s)
# s.extend("add")
# print(s)
# s.insert(-1, 'Hello')  # добавляем элемент (второй параметр) в список в заданный индекс (первый параметр)
# print(s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
#
# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []  # [2, 1, 4, 3]
#
# for i in a:  # 5, 9, 2, 1, 4, 3
#     for j in b:  # 4, 2, 1, 3, 7
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# for element in a:
#     if element not in c and element in b:
#         c.append(element)
#
# print(c)


# a = [1,2,3]
# b = [11, 22, 33]
# c = []

# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):  # 0-3
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):  # range(3, 5)
#     c.append(b[i])
# print(c)

# if len(b) > len(a):
#     for i in range(len(a)):  # 0-3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3, 5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0-3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # range(3, 5)
#         c.append(a[i])
# print(c)

# удаление по значению

# a = [1, 3, 2, 3, 4, 3, 5]
# print(a)
# a.remove(3) # удаление по значению
# print(a)
# n = 2
# if n in a:
#     a.remove(n)
# print(a)
#
# last = a.pop()


# n = [int(input("введите элементы списка: ")) for i in range(int(input("n = ")))]
# k = int(input("Введите индекс: "))
# print("k=", k)
# n.pop(k)
# print(n)


# a = [1, 3, 2, 3, 4, 3, 5]
# num = a.count(3)
# ind = a.index(2)
#
# a.sort(reverse=True) # сортировка списка по возрастанию(false) или (true)

# s = ["vity", "sasha", "alex"]
# s.sort(reverse=True, key=len)
# print(s)

# a = [1, 3, 2, 3, 4, 3, 5]
# a.sort()
# sorted(a)

# a = [1, 2, 3 ]
# b = a.copy() # возвращает копию списка
# a.append(20)
# b.append(120)


# генерация случайных данных

# import random
#
# print(random.random())  # от 0 до 1(не вкл)
# print(random.randint(0, 9))  # от 0 по 9(вкл)
# print(random.randrange(2,9, 2))  # randrange(start, stop, step)) (0,9)
# print(round(random.uniform(10.5, 25.5), 2))
# city_list= ["moscow", "ufa", "sochi"]
# print(random.choice(city_list))
#
# s =[2, 3, 4, 5]
# print(random.choice(s))
#
# print(random.choices(city_list, k=3))  # 3 elements
# print(random.shuffle(s))

# mas = [random.randint(0,100) for i in range(10)]
# print(mas)
# print(len(mas))
# print(min(mas))
# print(max(mas))
# print(sum(mas))

# n = [random.randint(0, 100) for i in range(10)]
# print(n)
# a = max(n)
# print(a)
# n.remove(a)
# n.insert(0, a)
# print(n)

# n = [random.randint(-20, 20) for i in range(10)]
# print(n)
# n.sort(reverse=True)
# print(n)

# n = [random.randint(0, 100) for i in range(10)]
# print(n)
# a = min(n)
# print(a)
# b = n.index(a)
# print("index min: ", b)
# print(n[b:])


# lst = [2]
# if len(lst) == 0:
#     if not lst:
#     print("пустой")
# print(5 not in lst)
#
# n1 = int(input("введите размер 1 списка"))
# n2 = int(input("введите размер 2 списка"))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("первый список:", a)
# print("второй список:", b)
# c = a + b
# print(c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("без пов", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print(c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print(len(m))
# print(m[1][2])
# print()
#
# for row in range(len(m)):
#     print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
#
# for row in m:
#     print(row)
#     for x in row:
#         print(x, end="\t")
#     print()


# w, h = 5, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
#
#
#
# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, y)


# import random

# w, h = 3, 4
# count = 0
# matrix = [[random.randint(-20, 20) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#             count += 1
#     print()
# print("Количество отрицательных элементов:", count)


# Modules

# import math
#
# print(math.sqrt(4))
# print(math.pi)
# print(math.ceil(3.2))  # 4
# print(math.floor(3.2))  # 3
#
# import math as m
#
# print(m.ceil(3.2))  # 4
# print(m.floor(3.8))  # 3

# from math import ceil, floor
#
# print(ceil(3.2))  # 4
# print(floor(3.8))  # 3

# from math import *
#
# print(ceil(3.2))  # 4
# print(floor(3.8))  # 3


# from math import pi
#
# radius = int(input("введите радиус окр"))
# print("длина  окр: ", round(2 * pi * radius, 2))
#
# from math import sqrt
#
# a = int(input(" катет 1: "))
# b = int(input(" катет 2: "))
# print("гипотенуза:", sqrt(a**2 + b**2))

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru_RU")
#
# second = time.time()
# print(time.ctime())
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("Today is %B %d, %Y", time.localtime(46367637658)))
# print(time.strftime(" %d/%m/%Y, %H:%M:%S"))
#
# pause = 5
# print("запущена")
# time.sleep(pause)
# print(pause, "sec")
#
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# def hello(name):
#     print("hello", name)
#
#
# hello("ira")
# hello("sam")
#
# def get_sum(a,b):
#     print("hello")
#     return a + b
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("adf", "dhf")


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
# m = maximum(9,6)
# print(m)


# def max(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
# c = int(input("a: "))
# d = int(input( "b: "))
# m = max(c , d)
# print(m)


# def cube(a):
#     return a*a*a
#
# for i in range(1,11):
#     print(i, " в кубе: ", cube(i))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["c", "l", "o", "n"]))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
# print(func(10, 5))
# print(func(5, 10))
# a = 10
# b = 5
# if func(a, b):
#     print("1>2")
# else:
#     print("2>1")


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":  # 65 <= 97 <= 90
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("введите пароль: ")
# if check_password(p):
#     print("это надежный пароль")
# else:
#     print("это ненадежный пароль")


# def get_sum(a, b, c, d=1):
#     return a + b+c+d
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(2, 5, 7))


# def set_param(c=20, s="-"):
#     print(s*c)
#
#
# set_param()
# set_param(7)
# set_param(s="#")


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 100322
#
#     return s
#
# print("сумма четных чисел:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
#
# print("сумма нечетных чисел:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")


# a = "hello"
# b = "hello"
# print(a == b)  # True
# print(a is b)  # True
# print(a, id(a))
# print(b, id(b))
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1 == lst2)  # True
# print(lst1 is lst2)  # False
# print(lst1, id(lst1))
# print(lst2, id(lst2))


# Изменяемые объекты - list
# Неизменяемые объекты - int, float, bool, str, tuple

# Кортежи (tuple)

# lst= [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = "red", "blue", "green"
# print(a)
# print(type(a))
#
# a = (5,)
# print(a)


# a = tuple("Hello")
# b = tuple([1, 5, 6])
# print(a[0])
# print(a[1:3])
# print(a)


# figure = input("1- , 2- ,3- :")
# if figure == 1:
#     rectangle()
# elif figure ==2:
#     triangle()


# Lesson 9


# s = tuple(i for i in range(5))
# print(s)
#
# res = tuple(2 **i for i in range(1, 12))
# print(res)
#
# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3 * 2)
# print(t3.count("l"))
# print(t3.index("l", 3))
#
# ch = "a"
# try:
#     print(t3.index(ch))
# except ValueError:
#     print("No value")
#
# for i in t3:
#     print(i, end="")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first +1)
#             return tpl[first:second +1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# from random import randint
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
# tpl = ran(0, 5)
# print(tpl)
# tpl2 = ran(-5, 0)
# print(tpl2)
# res = tpl + tpl2
# print(res)
# c = res.count(0)
# print(c)

# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))


# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# user = get_user()
# first_name, year, married = user
# first_name, year, married = get_user()
# print(user)
# print(user[0])


# def func(lst):
#     return sum(lst), len(lst)
#
#
# a, b = func([2, 9, 5, 6, 7, 8])
# print(func([2, 9, 5, 6, 7, 8]))
# print(a)
# print(b)


# lst = [1, 3, 5]
# tpl = tuple(lst)
# print(tpl)
# lst1 = list(tpl)
# print(lst1)


# countries = (
#     ("Germany", 80.2, (("Berlin", 3.326), ("Gamburg", 3.545))),
#     ("Ger", 80.2, (("Ber", 3.326), ("Gam", 3.545)))
#
# )
# print(countries)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nCOUNTRY", country_name, ",population= ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tcity:",city_name, "population:", city_population, sep="")


# Множество (set) - неупорядоченная коллекция, которая содержит только уникальные элементы

# s = {"banan", "apple", "orange", "apple"}
# print(len(s))
# for i in s:
#     print(i)
#
# s = ["banan", "apple", "orange", "apple"]
# st = set(s)

# a = set()
# print(type(a))

# s = {input("-> ") for i in range(5)}
# print(s)

# a = set("hello")
# print("o" in a)
# a.add("a")
# a.remove("e1")  # KeyError
# a.discard("o1")
# a.pop()
# a.clear()


# s = ["ab_1", 'ac_2','bc_1', 'bc_2']
# a = [i for i in s if 'a' not in i]
# a = ['A' + i[1:] if i[0] == 'a' else 'B'+ i[1:] for i in s]
# a = ['A' + i[1:] if i[0] == 'a' else 'B'+ i[1:] for i in s if i[1] == 'c']
# print(a)
# print(['A' + i[1:] if i[0] == 'a' else 'B'+ i[1:] for i in  ["ab_1", 'ac_2','bc_1', 'bc_2'] if i[1] == 'c'])


# тернарное выражение q = True if условие else False

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# a |= b  # a +=b
# c = a & b  # {1, 2, 3}
# a &= b
# c = a - b
# a -=b
# c = a ^ b  # unique from a and b
# a ^=b

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = "hello"
# s2 = "how are you"
# s = set(s1) & set(s2)
# print(s)
# for i in s:
#     print(i, end="")


# s1 = "Python"
# s2 = "Programming language"
# s = set(s1) - set(s2)
# print(s)
# for i in s:
#     print(i, end="")


# drawing = {"zhen", "sveta", "marina"}
# music = {"kosta", "zhen", "ilya"}
# one_hobby = drawing ^ music
# both_hobby = drawing & music
# drawing = drawing - both_hobby

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a >= b)
# print(a > b)


# frozenset
# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)


# Словарь (dict) - изменяемый тип

# s = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(s[1])
# print(d["two"])

# s1 = ["one", "two", "three"]
# d1 = {1: "one", 2: "two", 3: "three"}
# print(d1[2])

# d = {0: "test", "one": 45, (1, 2.3): "кортеж", True: 1, False: 35}  # set, list, False no!
# print(d[True])
# d[(1, 2.3)] = 100


# d = {'one': 1, 'two': 2}
# d1 = dict(one=1, two=2)
# d2 = dict([('one', 1), ('two', 2)])
#
# d = {x: x** 2 for x in range(7)}
# d = {"one": 1, "two": 2, "three": 3}
# print("two" in d)
# print(len(d))
# for key in d:
#     print(key, "->", d[key])
#
# key = "four"
# if key in d:
#     print(d[key])
#
#
# try:
#     print(d[key])
# except KeyError:
#     print("error")
#
#
# del d[key]
# print(d)


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# a = 1
# for i in d:
#     a *= d[i]
# print(a)


# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")

# d = {x: input("->") for x in range(1, 5)}
# print(d)
# try:
#     dislike = int(input("-?: "))
#     del d[dislike]
# except (KeyError, ValueError):
#     print("no key")
# print(d)


# goods = {
#     "1": ['Core-i3', 9, 4500],
#     "2": ['Core-i5', 3, 8500],
#     "3": ['AMD', 6, 3700],
#     "4": ['Pent', 8, 2100],
#     "5": ['Core-i5-34', 5, 6400]
# }
# for key in goods:
#     print(key, ") ", goods[key][0], "-", goods[key][1], "шт. по ", goods[key][2], "rub", sep="")
#
# while True:
#     n = input("#: ")
#
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("кол-во: "))
#                     goods[n][1] = count
#                     break
#                 except ValueError:
#                     print("error")
#         else:
#             print("error")
#     else:
#         break
#
# for key in goods:
#     print(key, ") ", goods[key][0], "-", goods[key][1], "шт. по ", goods[key][2], "rub", sep="")


# d = {'x1': 3, 'x2': 7, 'x3': 5}

# del d['x1']
# d['x4'] = 10
# a = {'one': 1}
#
# print(d.values())
# print(d.keys())
# print(d.items())
# for key, value in d.values():
#     print(key, "->", value)
#
# print(list(d))  # ['x1','x2','x3']
# print(list(d.values()))  # [3,7,5]
# print(list(d.items()))  # [('x1', 3) ...()]

# d = { 'x1': 3, 'x2': 7, 'x3': 5}
# d2 = d.copy()
#
#
# print("d=", d)
# print("d2=", d2)
#
# d2["x4"]= 10
# d["x1"] = 100
#
# print("d=", d)
# print("d2=", d2)


# d = { 'x1': 3, 'x2': 7, 'x3': 5}
# print(d["x1"])
# value = d.get("x1", "no key, error")
# print(value)
# item = d.pop("x1", "no key, error")
# item2 = d.popitem()  # key and value
#
# d.clear()  # all delete

# item3 = d.setdefault("x4", 10)  # add "x4": none (10)
# a = {"one": 1, "two": 2, "x1":10}
# a = list(a.items())
# a = [("one", 1), ("two", 2), ("x1", 10)]
# d.update(a)  # d+a


# x = {'a':1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x | y  # x+y
# z = x.copy()
# z.update(y)

# d = dict.fromkeys(["a", 'b', 'c'], 100)

# 1

# d = {'name': 'kelly', 'age': 25, 'salary': 8000, 'city': 'new york'}
# d2 = dict()
# d2['name'] = d.pop('name')  # value
# d2['salary'] = d.pop('salary')
# d['location'] = d.pop('city')
# print(d)

# d = {
#     'first': {
#         1: {
#             11: "abc"
#         },
#         2: {
#             11: "abc"
#         },
#         3: {
#             11: "abc"
#         }
#     },
#     'second': {
#         4: {
#             11: "abc"
#         },
#         5: {
#             11: "abc"
#         }
#     }
# }
# print(d)
#
# for x in d:
#     print(x)
#     for y in d[x]:
#         print("\t", y, ":", d[x][y])
#         for z in d[x][y]:
#             print("\t\t", z, ":", d[x][y][z])


# d = {'one':1, 'two':2, 'three':3, 'four': 4}
# d2 = {key: value for key, value in d.items()}
# d2 = {key: value for key, value in d.items() if value <=2}
# print(d2)
# d2[1], d2[4]= d2[4], d2[1]


# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = none
#
# for i in a:
#     if type(i)== str:
#         d[i] = []  # d['one']=[]
#         s = i  # s= 'one'
#     else:
#         d[s].append(i)  # d[1]
# print(d)


# zip()

# one = [1, 2, 3]
# two = ["one", "two", "three"]
# three = [2.5, 4.6, 8.9]
#
# d = dict(zip(one, two))
# print(d)
#
# lst = list(zip(one, two, three))
# lst = list(zip(one))
#
# f = {k: v for k, v in zip(one, two)}
# print(f)
#
#
# one = {"name": "ira", "surname": "koka", "job": "prog"}
# two = {"name": "iran", "surname": "kuki", "job": "pr"}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)


# lst = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*lst)
# print(a)
# print(b)


# a = {"one": 1, 'two':2, 'three':3}
# b = {'three':3, 'four':4}
# print({**a, **b})  # {"one": 1, 'two':2, 'three':3, 'four':4}
#
# for k, v in {**a, **b}.items():
#     print(k, "->", v)


# data = [5, 7, 9, 4, 1, 3, 5, 8, 6, 4]

# j = 1
# for i in data:
#     print(i, ")", i, sep="")
#     j +=1

# for j, i in enumerate(data, 1):
#     print(j, ")", i, sep="")


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]  # *a - распаковка
# print(b)

# def func(*args):
#     print(*args)
#     return args  # кортеж
#
# print(func(5))
# print(func(5, 6, 7, "abc"))
# print(func())

# def summa(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
# print(summa(1, 8, 9, 6, 4))


# def to_dict(*di):
#     # dictionary = {}
#     # for i in di:
#     #     dictionary.update({i:i})
#     #
#     # return dictionary
# #     return dict(zip(di, di))
#     return {i: i for i in di}
#
# print(to_dict(1,2,3,4))
# print(to_dict("grey", (2,17), 3.11, -4))


# def ch(*args):
#     average = sum(args) / len(args)
#     print(average)
#     lst = []
#     for i in args:
#         if i < average:
#             lst.append(i)
#     return lst
#
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
# print(func(5))
# print(func(5, 4,6,7))

# def print_csores(student, *scores):
#     print("Name:", student)
#     for score in scores:
#         print(score, end="")
#     print()
#
# print_scores("Boba", 5, 4, 5, 3, 5,5)
# print_scores("Nik", 5, 4, 5, 5)


# def func(**kwargs):
#     return kwargs
#
# print(func(a=1, b=2, c=3))
# print(func())

# def intro(**kwargs):
#     for k, v in kwargs.items():
#         print(k, "is", v)
#     print()
#
# intro(name="Ira", surnname = "dasda", age=22)
# intro(name="Iran", surnname = "daga", email = "rgfdgf@ilcoud.com", age=26, phone=8944663633)


# def func(a, b, *args,d=5,c=5, **kwargs):
#     return a, b, args, kwargs, d, c
#
# print(func(1,2,3,4,5, a=1, b=2, cc=3))


# def db(**kwargs):
#     my_dict.update(**kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k=22, k2=31, k3=45, k4=91)
# db(name="bob", age=31, weight=61, color="blue")
# print(my_dict)

# name = "Tom"  # глобальная переменная(видна внутри ф)
# surname= ""
# def hi():
#     global name, surname
#     name ="Sam"  #локальная переменная
#     surname = "Jonson"
#     print("hello", name, surname)
#
#
# def bye():
#     print("bye", name)
#
# hi()
# bye()
# print(name)




# i = 5
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5


# def func(a):  # a=3
#     x=2
#
#     def inner():
#         print('x:', x)
#         return a+x
#
#     return inner()
#
# print(func(3))




# sum = "Hello"
#
# print(sum)
#
# lst = [1, 2, 3, 4, 5, 6, 4]
# print(sum(lst))

# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World!")


# def fun1():
#     a = 6  # 2
#
#     def fun2(b):  # b = 4
#         a = 4  # 5  # a = 6
#         print(a + b)  # 6  # a + b = 8 (10)
#
#     print("a:", a)  # 3
#     fun2(4)  # 4
#
#
# fun1()  # 1

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         # print(a)
#
#     inner()
#     t = a  # 35
#
#
# fn()
# q = x + t  # 25 + 35
# print(q)  # 60

# x = 5


# def fn1():
#     x = 25  # 55
#
#     def fn2():
#         x = 33  # 55
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)  # 33  55
#
#     fn2()
#     print("fn1.x =", x)  # 25  55
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0  # 1
#     b = 0  # 7
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print("a:", a)
#         # print("b:", b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# Замыкание

# def outer(n):  # 5
#     def inner(x):  # 10
#         return n + x
#
#     return inner
#
#
# out1 = outer(5)
# print(out1(10))
#
# out2 = outer(6)
# print(out2(4))

# print(outer(5)(10))


# def func(a):
#     return a + 2
#
#
# var = func(5)
# print(var)


# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     count = 0  # 3  # 5
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
# res2()
# res2()
# res2()
#
# res1()
# res1()
# res1()
# res1()


# lambda - функция (выражение)

# def func(x, y):
#     return x + y
#
#
# print(func(2, 3))

# print((lambda x, y: x + y)(2, 3))
# print((lambda x, y: x + y)(12, 3))

# variable = lambda x, y: x + y
#
# print(variable(2, 3))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())

# print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6))
# print((lambda *args: args)("a", "b", "c"))


# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t("abc_"))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(5)
# print(f(10))


# def outer1(n):
#     return lambda x: n + x
#
#
# f1 = outer1(5)
# print(f1(10))
#
# outer2 = lambda n: lambda x: n + x
#
# f2 = outer2(5)
# print(f2(10))

# print((lambda n: lambda x: n + x)(5)(10))


# print((lambda n: lambda x: lambda y: n + x + y)(2)(4)(6))
# print((lambda n: lambda x: lambda y: n+x+y)(int(input("Введите 1 число: ")))(int(input("Введите 2 число: ")))
# (int(input("Введите 3 число: "))))


# def func(i):
#     return i[1]
#
#
# d = {"b": 15, "a": 7, "c": 3}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# # lst.sort(key=func)
# print(lst)
# print(dict(lst))


# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# s = 0
#
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(s)
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)


# def outer(a, b, c):  # 2, 4, 6
#     s = 0  # 44
#
#     def inner(i, j):
#         nonlocal s
#         s = s + i * j  # s += i * j   # s = 20 + 24 = 44
#
#     inner(a, b)  # 2, 4
#     inner(a, c)  # 2, 6
#     inner(b, c)  # 4, 6
#     return 2 * s  # 2 * 44
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))


# players = [
#     {'name': 'Антон', 'last_name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last_name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last_name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last_name': 'Семенов', 'rating': 6},
# ]
#
# res1 = sorted(players, key=lambda item: item['last_name'])
# print(res1)
# res2 = sorted(players, key=lambda item: item['rating'])
# print(res2)
# res3 = sorted(players, reverse=True, key=lambda item: item['rating'])
# print(res3)

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y]
# b = a[0](5, 3)
# print(b)


# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
# }
#
# d[3]()

# print((lambda a, b: a if a > b else b)(5, 13))


# print((lambda a, b, c: a if (a < b) and ((b < c) or (b > c)) else b if b < c else c)(12, 15, 6))


# print((lambda a, b, c: a if (a < b) and (a < c) else b if (b < c) and (b < a) else c if (c < a) and (
#             c < b) else "Ну тут уже всё:)")(22, 35, 16))
# print((lambda a, b, c: a if (a < b) and (a < c) else b if (b < c) and (b < a) else c)(12, 36, 15))
#
# print((lambda a, b, c: a if min(a, b, c) == a else b if min(a, b, c) == b else c if min(a, b,

#  c) == c else "Несколько равных")(
#     11, 2, 111))
#
# print((lambda *args: min(args))(12, 5, 6))
# print((lambda *args: sorted(args)[0])(2, 5, 6))
# print((lambda *args: sorted(args)[-1])(2, 5, 6))

# map(func, iterable), filter(func, iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# lt = list(map(mult, lst))
# print(lt)
#
# lt1 = list(map(lambda t: t * 2, lst))
# print(lt1)
#
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))

# lst = ['1', '2', '3', '4', '5']
# print(lst)
# print(list(map(lambda x: int(x), lst)))
# print([int(i) for i in lst])
# print(list(map(int, lst)))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: {x: y}, st, num)))

# st = [9, 2, 7, 6, 5]
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: x + y, st, num)))

# t = ('abcd', 'abc', 'cdefg', 'def', 'gth', '', False)  # 'abcdabcdabcd'
#
# # t2 = list(filter(lambda s: len(s) == 3, t))
# t2 = list(filter(lambda s: s, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, b)))

# от 1 до 40

# from random import randint
#
# arr = [randint(1, 40) for i in range(10)]
# print(arr)
# # print(list(filter(lambda a: (a >= 10) and a <= 20, arr)))
# print(list(filter(lambda a: 10 <= a <= 20, arr)))

# Вывести на экран квадраты нечетных чисел от 1 до 10
# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))
# print([x ** 2 for x in range(1, 10) if x % 2])


# Декораторы

# def hello():
#     return 'Hello, I am func "hello"'  # 3
#
#
# def super_func(func):  # (def hello(): return 'Hello, I am func "hello"')
#     print('Hello, I am func "super_func"')  # 2
#     print(func())  # 4
#
#
# super_func(hello)  # 1


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(id(test))
# print(id(hello))
# print(test())

# def my_decorator(func):
#     def inner():
#         print('Code before')
#         func()
#         print('Code after')
#     return inner
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def inner():
#         print('*' * 40)
#         func()
#         print('-' * 40)
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# @my_decorator
# def hello():
#     print('Hello, I am func "hello"')
#
#
# func_test()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Мумладзе")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def func(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# @args_decorator
# def func1(study):
#     print("Мне нравится", study)
#
#
# func("Борис", "Елизавета", "Светлана", study="JavaScript")
# func("Владимир", "Екатерина", "Виктор")
# func1(study="HTML")

# def decor_args(arg1, arg2):
#     def decor(fn):
#         def wrap(x, y):
#             print(arg1, x, arg2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return decor
#
#
# @decor_args("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor_args("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def decor_args(arg1):
#     def decor(fn):
#         def wrap(x):
#             return arg1 * fn(x)  # 3 * 5
#
#         return wrap
#     return decor
#
#
# @decor_args(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# Строки

# print(int("19"))
# print(int("19.5"))
# print(int(19.5))

# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))


# print(bin(18))  # 0b10010 - двоичная
# print(oct(18))  # 0o22 - восьмеричная
# print(hex(18))  # 0x12 - шестнадцатеричная
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0b10010 + 0x12)


# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 2)
# print("y1" in e)
# print(e[0])
# print(e[1:3])

# s = "Python"  # Pytton
# # s[3] = "t"
# s = s[:3] + 't' + s[4:]
# print(s)

# def change_char_to_str(s, old, new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == old:
#             s2 = s2 + new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = change_char_to_str(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)

# print("Привет")
# print(u"Привет")

# print("C:\\folder\\fil\nes.txt\\")
# print(r"C:\folder\files\\"[:-1])
# print(r"C:\folder\files" + "\\")

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

# ch = 5.26987412
#
# print(f"Число: {round(ch, 3)}")
# print(f"Число: {ch:.3f}")

# x = 10
# y = 5
# print(f"{x = }, {y = }")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# num = 74
#
# print(f"{{{{{num}}}}}")
#
# print("C:\\\\text")

# dir_name = 'my_doc'
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)


###########################################################################
# def avg(fn):
#     def wrap(*arg):
#         a = ""
#         for i in arg:
#             a += str(i) + ", "  # "2, 3, 3, 4, "
#         print("Среднее арифметическое:", a[:-2], "=", fn(*arg) / len(arg))
#
#     return wrap
#
#
# @avg
# def summa(*args):  # (2, 3, 3, 4)
#     print("Сумма чисел:", ", ".join(map(str, args)), "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)
###########################################################################

# s = """
# Несколько
# строк
# """
# # print(s)
#
# s1 = '''
# Несколько
# строк
# '''
# print(s1)
#
# "Несколько строк"
# print(s2)


# def square(n):
#     """Принимает число n, возвращает квадрат числа n."""
#     print()
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# # max(5, 5)
# # len()
# print(len.__doc__)


# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)
# print(max.__doc__)
# print(dict.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('й'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# s = "Test string for me"
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(8364))

# a = 97
# b = 122
#
# if a < b:
#     a, b = b, a
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# print("apple" == "Apple")
# print("apple" > "Apple")  # 97 > 65


# from random import randint
#
# shortest = 7
# longest = 16
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     res = ""
#     for i in range(randint(shortest, longest)):  # range(10)
#         rand_char = chr(randint(min_ascii, max_ascii))
#         res += rand_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())


# s = "hello, WORLD! I am learning Python."
# # print(s.capitalize())  # Hello, world! i am learning python.
# # print(s.lower())  # hello, world! i am learning python.
# # print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# # # print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# # # print(s.title())  # Hello, World! I Am Learning Python.
# # print(s)
#
# # print(s.count("l"))
# # print(s.count("l", 3))
# # print(s.count("l", 3, 10))
#
# # print(s.find("Python1"))  # возвращает индекс первого вхождения подстроки в строку, если такой подстроки нет
# # # возвращает "-1"
# # # print(s.find("l", 4, 20))
# # print(s.find("l"))
# # print(s.rfind("l"))
# #
# # print(s.index("l"))  # ValueError
# # print(s.rindex("l"))
#
#
# # st = input("Введите два слова через пробел: ")
# # first = st[:st.find(" ")]
# # second = st[st.find(" ") + 1:]
# # print(second + " " + first)
# print(s.startswith("I am", 14))
# print(s.index("I am"))
# print(s.endswith("on."))


# print(int("789"))

# print('123'.isdigit())  # только числа
# print('qЙwee'.isalpha())  # только буквы
#
# print('Abc123'.isalnum())  # только буквы или цифры
#
# print('aИc0123"№'.islower())  # только нижний регистр
# print('ASD0123"№'.isupper())  # только верхний регистр

# n = input("Введите число: ")
# if n.isdigit():
#     n = int(n)
#     print(n * 2)


# print('py'.center(10))
# print(' py '.center(11, "-"))


# print('    py    '.lstrip())
# print('    py    '.rstrip())
# print('    p y    '.strip())
#
# print('https://www.pythons.org'.strip('/:pths.org'))
# print('https://www.pythons.org'.lstrip('/:pths').rstrip('.org'))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования. New"
# print(str1.replace("Nython", "Python"))
# print(str1.replace("N", "P"))


# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '99']))
#
# print(", ".join("Hello"))

# print("Строка разделенная пробелами".split())  # ['Строка', 'разделенная', 'пробелами']
# print('www.python.org.ru'.split(".", 2))
# print('www.python.org.ru'.rsplit(".", 2))

# a = input("-> ").split()
# b = list(map(int, a))
# print(b)




# Регулярные выражения

# import re

# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта."
# reg = "а"

# print(re.findall(reg, s))  # возвращает список содержащий все совпадения
#
# print(re.search(reg, s))  # месторасположение первого совпадения с объектом
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
#
# print(re.match(reg, s))  # поиск совпадения с шаблоном вначале строки
#
# print(re.split(reg, s, 1))  # возвращает список, в котором строка разбита по шаблону
#
# print(re.sub(reg, "!", s, 2))  # поиск и замена

# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё-та. 198673 Hello"
# reg = "[21][0-9][0-9][0-9]"
# reg = "[А-яЁё]"
# reg = "[A-Za-z]"
# reg = r"\."
# reg = r"[A-Za-z\[\]-]"
# reg = r"[^0-9]"
# reg = r"[^А-яЁёA-Za-z0-9]"
# print(re.findall(reg, s))

# print(ord('Я'))
# print(ord('а'))


# st = "Час в 24 формате от 00 до 23. 2021-06-15T19 : 30. Минуты, в диапазоне от 00 до 59. 2021-06-15T01 : 09."
# pattern = r"[0-2][0-9]\s:\s[0-5][0-9]"
# print(re.findall(pattern, st))


# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё-та. 198673 Hel_lo 20000000000000000000000000"
# reg = r"[20]*"
# print(re.findall(reg, s))

# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1

# d = "Цифры: 7, +17, --42, 0013, 0.3"
# reg = r'[+-]?[\d.]+'
# print(re.findall(reg, d))


# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"\s#.*", "", s))
# print(re.sub('-', '.', s))
# print("Дата рождения:", re.sub('-', '.', re.sub(r"\s#.*", "", s)))
# # print("Дата рождения:", "05.03.1987")
# # Дата рождения: 05.03.1987
# print("Дата рождения", re.sub("-", ".", re.sub("\\s#.*", "", s)))

# s = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# reg = r'\w+\s*=\s*[^;]+'
# # reg = r'[^;]+'
# print(re.findall(reg, s))

# s = "12 сентября 2024 года 568789456"
# reg = r"\d{2,4}"
# print(re.findall(reg, s))


# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё_та."
# # reg = r"^\w+\s\w+"
# reg = r"\w+\.$"
# print(re.findall(reg, s))

# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9-]{3,16}$", login)
#
#
# print(validate_login("Python-master"))



# s = "+7 499 456-45-78, +74994564578, 7 (499) 4564578, 74994564578, +24994564578"
#
# reg = r"\+?7\d{10}"
# print(re.findall(reg, s))

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "Hello world"
# print(re.findall(r"\w\+", text, re.DEBUG))

# s = "Я ищу совпадение в 2024 году. И я их найду в 2 счёта."
# reg = "я"
#
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.findall(reg, s, re.I))

# text = """
# one
# two
# """

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall('''
# [A-Za-z0-9._-] +   # part 1
# @                  # @
# [A-Za-z.-]+        # part 2
# ''', 'test@mail.ru', re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
#
# reg = "(?mi)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))

# +?, *?, ??
# {m,n}?, {,n}?, {m,}?

# s = "12 сентября 2024 года 568789456"
# reg = r"\d{2,4}?"
# print(re.findall(reg, s))

# s = "Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0, float"
# reg = r"\w+\s*=\s*\d[.\w]*"
# reg = r"int\s*=\s*\d[.\w]*|float\s*=\s*\d[.\w]*"
# reg = r"(?:int|float)\s*=\s*\d[.\w]*"
# reg = r"(int|float)\s*=\s*\d[.\w]*"
# print(re.findall(reg, s))
# print(re.search(reg, s))

# (?: ....) - группирующая скобка не является сохраняющей

# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# s = "01-12-2024"
# reg = "(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# # print(re.findall(reg, s))
# # print(re.search(reg, s).group())
# # m = re.search(reg, s)
# # print(m[0])
# # print(m[1])
# # print(m[2])
# # print(m[3])
# print(re.search(reg, s).group())
# print(re.search(reg, s).group(1))
# print(re.search(reg, s).group(2))
# print(re.search(reg, s).group(3))

# text = """
# Самара
# Москва
# Тверь
# Цфа
# Казань
# """
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", replace_find, text))

# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024."  # 23.10.2024  24.10.2024
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r"([a-z0-9-]{2,}\.[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))  #


# Рекурсия

# def elevator(n):  # 0
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)  # 1
#     elevator(n - 1)  # 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def to_str(n, base):  # 2, 10
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # convert[15] = 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] = 'E'
#
#
# print(to_str(254, 10))  # to_str(254, 16) => FE


# names = ["Adam", ["Bob", ["Chet", "Cat", ["1", ["2", ["3"]]]], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# # print(names[0])
# # print(isinstance(names[0], list))
# # print(names[1])
# # print(isinstance(names[1], list))
# # print(names[1][1])
# # print(isinstance(names[1][1], list))
# def count_items(item_list):
#     count = 0  # 10
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)  # count += 2
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# def remove(text):  # ""
#     if not text:  # text = ""
#         return ""
#     if text[0] == "\n" or text[0] == " ":
#         return remove(text[1:])  # ""
#     else:
#         return text[0] + remove(text[1:])  # "HelloWorld" + ""
#
#
# print(remove("  Hello\nWorld "))


# Файлы

# f = open("test.txt", "r")
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()
# print(f.closed)


# f = open("test.txt", "r")
# # f = open(r"D:\Python317\317\test.txt", "r")
# print(f.read(3))
# print(f.read())  # возвращает весь документ
# f.close()


# f = open("test2.txt", "r")
# print(f.readline())  # возвращает одну строку
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()


# f = open("test2.txt", "r")
# print(f.readlines(16))
# print(f.readlines())  # возвращает список строк
# f.close()

# f = open("test2.txt", "r")
# count = 0
# for line in f:
#     print(line, end="")
#     count += 1
# f.close()
# print(count)

# f = open("test2.txt", "r")
# print(len(f.readlines()))
# f.close()

# f = open("xyz.txt", "w")
# f.write("Hello\nWorld!\n")
# f.close()


# f = open("xyz.txt", "a")
# f.write("New text.\n")
# f.close()


# f = open("xyz.txt", "a")
# lines = ['\nThis is line 1', '\nThis is line 2']
# f.writelines(lines)
# f.close()

# f = open("xyz.txt", "w")
# lst = [str(i) + " " for i in range(1, 20)]
# print(lst)
# # for index in lst:
# #     f.write(index + "\t")
# f.writelines(lst)
# f.close()


# f = open("test3.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл\n")
# f.close()

# f = open('test3.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = "Hello world!\n"
# print(read_file)
# f.close()
#
# f = open("test3.txt", "w")
# f.writelines(read_file)
# f.close()


# f = open("test3.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл\n")
# f.close()

# f = open("test3.txt", 'r')
# read_file = f.readlines()
# pos = int(input("Введите индекс строки для удаления: "))
# if 0 <= pos < len(read_file):
#     del_pos = read_file.pop(pos)
# else:
#     print("Индекс введен неверно")
# f.close()
#
# f = open("test3.txt", 'w')
# f.writelines(read_file)
# f.close()


# f = open("test.txt", "r")
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию условного курсора в файле
# print(f.seek(1))  # перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("test.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# f = open("test2.txt", "a+")
# # print(f.write("1111 I am learning Python 1111"))
# print(f.read())
# f.close()

# with open("test2.txt", 'w+') as f:
#     print(f.write('01234\n56789'))
# print(f.closed)


# with open("test2.txt", 'r') as f:
#     for line in f:
#         print(line[:3])

# def negative_numbers(n):  # n = []
#     if not n:
#         return 0
#     count = 0  # 0
#     if n[0] < 0:
#         count += 1
#     return negative_numbers(n[1:]) + count  # 1 + 0 + 0 + 1 + 1 + 0 + 0
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(negative_numbers(lst))

# file_name = "res.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = map(str, lt)  # ['4.5', '2.8', '3.9', '1.0', '0.3', '4.33', '7.777']
#     return ' '.join(lt)  # "4.5 2.8 3.9 1.0 0.3 4.33 7.777"
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
# #     # f.write(str(lst))  # "4.5 2.8 3.9 1.0 0.3 4.33 7.777"
#
#
# with open(file_name, 'r') as f:
#     st = f.read()
#
# print(st)
# print(type(st))
#
# nums = list(map(float, st.split()))
# print(nums)
# print(type(nums[0]))

# a = 5


# if a == 5:
#     b = 10

# for i in range(12):
#     b = 10

# def func():
#     b = 10
#
#
# func()
# print(b)

# def longest_worlds(file):
#     with open(file, 'r') as text:  # encoding="utf-8"
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         print(max_length)
#         res = [i for i in w if len(i) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_worlds('test.txt'))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\n
# Строка №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)


# with open('one.txt', 'r') as fr, open('two.txt', 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)


# Модуль OS, OS.PATH

# import os

# import os.path

# print(os.getcwd())  # возвращает текущую директорию
# print(os.listdir())  # список директорий и файлов
# print(os.listdir(".."))

# os.mkdir("folder1")  # создает папку
# os.makedirs("nested1/nested2/nested3")  # создает конечную директорию вмести с промежуточными

# os.rmdir("folder1")  # удаление пустой папки
# os.rmdir("nested1/nested2/nested3")

# os.remove("xyz1.txt")  # удаление файла

# os.rename("xyz.txt", "new.txt")  # переименование файла и папки
# os.rename("folder", "new")

# os.rename("two.txt", "nested1/two1.txt")
# os.renames("test.txt", "nested1/nested3/two.txt")  # переименование файла и папки, перемещает документы,
# создавая промежуточные директории


# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root:", root)
#     print("\tSubdirs:", dirs)
#     print("\t\tFiles:", files)


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print('-' * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print('-' * 50)
#
#
# remove_empty_dirs("nested1")

# print(os.path.split(r"D:\Python317\317\nested1\nested2\nested4\text.txt"))  # [1]
#
# print(os.path.join('nested4', r'D:\Python317', '317', 'nested1', 'nested2', 'text.txt'))

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1, file)
#         open(file_path, 'w').close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"Текст в файле {file}")

# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

