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

d = {x: input("->") for x in range(1, 5)}
print(d)
try:
    dislike = int(input("-?: "))
    del d[dislike]
except (KeyError, ValueError):
    print("no key")
print(d)