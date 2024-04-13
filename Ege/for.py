# 1
# s = "3"*30
# while "333" in s or "555" in s:
#     if "333" in s:
#         s = s.replace("333", "5", 1)
#     else:
#         s = s.replace("555", "3", 1)
# print(s)


# 2
# s = "1"*9+"2"*22
# while "111" in s or "222" in s:
#     while "111" in s:
#         s = s.replace("111", "2", 1)
#     while "222" in s:
#         s = s.replace("222", "1", 1)
# print(s)


# 3
# s = "5"+ "4"*99
# while "54" in s or "644" in s or "7444" in s:
#     if "54" in s:
#         s = s.replace("54", "6", 1)
#     else:
#         if "644" in s:
#             s = s.replace("644", "7", 1)
#         else:
#             s = s.replace("7444", "5", 1)
# print(s)

# 4
# s = "3"*76+"5"*24
# while "3333" in s or "5555" in s:
#     if "3333" in s:
#         s = s.replace("3333", "55", 1)
#     else:
#         s=s.replace("5555", "33", 1)
# print(s)

# 5
# s = "1"+"4"*81
# while "14" in s or "244" in s or "3444" in s:
#     if "14" in s:
#         s = s.replace("14", "3", 1)
#     if "244" in s:
#         s=s.replace("244", "1", 1)
#     if "3444" in s:
#         s= s.replace("3444", "2", 1)
# print(s)

# 6
# s = "9"*561
# while "999" in s or "666" in s:
#     if "999" in s:
#         s = s.replace("999", "6", 1)
#     else:
#         s = s.replace("666", "9", 1)
# print(s)

# 7
# s = "123"* 456
# while "12" in s or "3333" in s:
#     s = s.replace("12", "3", 1)
#     s = s.replace("3333", "3", 1)
# print(s)

# 8
# s = "1"+ "8"*80
# while "18" in  s or "288" in s or "3888" in s:
#     if "18" in s:
#         s = s.replace("18", "2", 1)
#     else:
#         if "288" in s:
#             s =s.replace("288", "3", 1)
#         else:
#             s = s.replace("3888", "1", 1)
# print(s)


# система счисления


# print(bin(11)[2:])  #2
# print(oct(11))  # 8
# print(hex(123))  # 16

# x = 11
# while x>0:  # 10->2
#     print(x % 3)
#     x = x // 3
#
# print(int("1223", 2))  # 2-> 10 or 8-> 10


# 14

# s = 4096 * 8 + 512 * 64 - 64 ** 512
# print(oct(s)[3:].count("7"))
#
# s = 1234 * 1234 + 456 * 456
# print(bin(s)[2:].count("1"))
#
# s = 234 * 123 + 32 ** 12 - 32
# cnt3 = 0
# while s > 0:
#     if s % 4 == 3:
#        cnt3 +=1
#     s = s // 4
# print(cnt3)

# 14

# 222(x) + 17(8)= 238(9)
# for x in range(3, 10):
#     if (int("222", x) + int("17", 8))== int("238", 9):
#         print(x)


# 14

# for x in "0123456789ABCDEFGHI":
#     if (int("11A" + x + "3", 19) + int("12" + x + "345", 19)) % 14 == 0:
#         print(x, (int("11A" + x + "3", 19) + int("12" + x + "345", 19)) // 14)


# 14

# s =64**2023 + 32**2022 -8**2021 -2
# print(hex(bin(s)[2:].count("1")))


# 14
# s =64**2023 + 32**2022 -8**2021 -2
# digits = []
# while s >0:
#     digits.append(s%20)
#     s = s // 20
# print(digits[::-1])


# 14

# s = 1331**1331 - 120*121**121 + 140*121**110 - 15*11**111 - 1221
# digits = []
# while s >0:
#     digits.append(s%11)
#     s = s //11
# print(digits.count("10"))


# 14

# for n in range(3, 10):
#     if int("121", n+1) == int("121", n) + int("13", 16):
#     print(n)


# 14

# for x in "0123456789ABCDEFGH":
#     if (int("2671" + x, 18) + int("8513" + x, 18)) % 13 ==0:
#         a = (int("2671" + x, 18) + int("8513" + x, 18)) // 13
# print(a)

# 14

# for x in "0123456789ABCDEF":
#     if (int("D49" + x + "1", 16) + int("48A3" + x, 16)) %14 == 0:
#         print(x, (int("D49" + x + "1", 16) + int("48A3" + x, 16)) // 14)


# 14

# from string import *
#
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# for x in "0123456789ABCDEFGHIJKLMNOPQ":
#     if (int(f"{x}1{x}2{x}3{x}4{x}5", 27) + int(f"20{x}204", 27) + int(f"20{x}20", 27)) % 25 == 0:
#         print((int(f"{x}1{x}2{x}3{x}4{x}5", 27) + int(f"20{x}204", 27)+ int(f"20{x}20", 27)) // 25)


# 14
# 654x(37) + 5x47(37)
# for x in range(0,37):
#     if ((6*37**3 + 5*37**2 + 4*37**1 + x*37**0) + (5*37**3 + x*37**2 + 4*37**1 + 7*37**0)) % 79 == 0:
#         print(((6*37**3 + 5*37**2 + 4*37**1 + x*37**0) + (5*37**3 + x*37**2 + 4*37**1 + 7*37**0)) // 79)


# 14
# for x in "0123456789ABCDEFGHIJKLMNOPQ":


# for i in range(151, 1000):
#     a = "7" * i
#     while "777" in a:
#         a = a.replace("777", "111", 1)
#         a = a.replace("1111", "7", 1)
#     if a == "711":
#         print(i)
#         break

# Combinatorika

# from itertools import *
#
# numb = 1
# for i in product("АДИН", repeat=5):
#     word = "".join(i)
#     if word == "ДИАНА":
#         print(numb, word)
#     numb += 1


# from itertools import *
#
# numb = 1
# for i in product("EMNOY", repeat=5):
#     if numb == 1055:
#         print(i)
#     numb +=1


# x = 1054
# digit = []
# while x > 0:
#     digit.append(x % 5)
#     x = x // 5
# print(digit[::-1])


# from itertools import *
# cnt = 0
# for i in product("XIAIO", repeat=8):
#     if i.count("I") ==3:
#         cnt+=1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in product("KEPN", repeat=6):
#     if i.count("E") >=1:
#         cnt+=1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in permutations("ДИС", r=7):
#     if i[0]!= "П":
#         cnt +=1
# print(cnt)


# from itertools import *
# cnt = 0
# for i in permutations("МАСЛО", r=5):
#     if i[0]!= "С" and "МО" not in "".join(i):
#         cnt +=1
# print(cnt)


# from itertools import *
#
# cnt = 0
# for i in permutations("KAPT", r=3):
#     if i[-1] != "P" and "KT" not in "".join(i):
#         cnt += 1
# print(cnt)


# Черепаха


# from turtle import *
# tracer(0)
# left(90)
# pendown()
# k = 30
# for i in range(16):
#     forward(5*k)
#     left(70)
#     backward(2*k)
#     right(10)
# penup()
# for x in range(-10,10):
#     for y in range(-10,10):
#         setpos(x*k,y*k)
#         dot(4)
# done()


# 8

# from itertools import *
#
# gl = "АЕО"
# sogl = "БНДРЛ"
# cnt = 0
# for i in product("БАНДЕРОЛЬ", repeat=7):
#     if sum(i.count(x) for x in gl)> sum(i.count(x) for x in sogl):
#         cnt+=1
#
# print(cnt)


# 16

import sys

sys.setrecursionlimit(3000)


# def F(n):
#     if n <= 14:
#         return n * n * n + 22
#     if n % 3 == 0 and n > 14:
#         return F(n - 4) + F(n - 8)
#     if n % 3 != 0 and n > 14:
#         return F(n - 9) + n + 7
#
#
# cnt = 0
# for n in range(1, 200):
#     if "1" not in str(F(n)) and "3" not in str(F(n)) and "5" not in str(F(n)) and "7" not in str(F(n)) \
#             and "9" not in str(F(n)):
#
#         cnt += 1
#
# print(cnt)


# def F(n):
#     if n <= 4:
#         return n
#     if n % 2 == 0 and n > 4:
#         return n + 4 * F(n - 1)
#     if n % 2 != 0 and n > 4:
#         return 2 * n * n * n + F(n - 1)
#
#
# cnt = 0
# for n in range(1, 401):
#     if F(n) % 8 == 0:
#         cnt += 1
#
# print(cnt)

# from functools import lru_cache
#
# @lru_cache
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 3 * F(n - 1) + 2 * G(n - 1) +n*n
#
# @lru_cache
# def G(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * F(n - 1) + 3 * G(n - 1) + n * 5
#
#
# summ = 0
# for n in str(G(222)):
#     summ += int(n)
#
# suma = 0
# for i in str(F(333)):
#     suma += int(i)
# print(abs(summ - suma))


# def task(start, end, k):
#     if start > end or (start == end and k < 2):
#         return 0
#     if start == end and k == 2:
#         return 1
#     if k == 2:
#         return task(start + 2, end, k) + task(start + 3, end, k)
#     if k < 2:
#         return task(start + 2, end, k) + task(start + 3, end, k) + task(start * 2, end, k + 1) + \
#             task(start * 3, end, k + 1)
#
#
# print(task(1, 51, 0))


# 2


# print("x y z w F1 F2")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 F1 = (x <= w) == (z <= y)
#                 F2 = (x <= w) and ((not (y)) == z)
#                 print(x, y, z, w, int(F1), int(F2))

# 17

# f = open("17.3.txt")
# a = [int(s) for s in f]
# mina = min(a)
# sum_par = []
#
# for i in range(len(a) - 1):
#     if a[i] % 123 == mina or a[i + 1] % 123 == mina:
#         sum_par.append(a[i] + a[i + 1])
# print(len(sum_par), max(sum_par))


# f = open("")
# a = [int(s) for s in f]
# maxi = max([x for x in a if str(x)[-1] == "6"])
# summ = []
# for i in range(len(a) - 1):
#     if (str(a[i])[-1] == "6" + str(a[i + 1])[-1] == "6") == 1 and (a[i] ** 2 + a[i + 1] ** 2)<maxi**2:
#         summ.append(a[i] ** 2 + a[i + 1] ** 2)
# print(len(summ), max(summ))


# f = open("PDF_8209_dokument.pdf")
# a = [int(s) for s in f]
# min = min([x for x in a if len(str(x)) == 2])
# summ = []
# for i in range(len(a) - 1):
#     if len(str(a[i])) == 2 and len(str(a[i + 1])) == 2 and (a[i] + a[i + 1]) % min == 0:
#         summ.append(a[i]+a[i+1])
# print(len(summ), max(summ))


# f = open("PDF_8209_dokument.pdf")
# a = [int(s) for s in f]
# max = max([x for x in a if str(abs(x))[-2:] == "13"])
# summ = []
# for i in range(len(a) - 2):
#     if int(len(str(abs(a[i])))==5) + int(len(str(abs(a[i + 1])))==5) + int(len(str(abs(a[i + 2])))==5) == 2 and (
#             a[i] + a[i + 1] + a[i + 2]) <= max:
#         summ.append(a[i] + a[i + 1] + a[i + 2])
# print(len(summ), max(summ))


# 15


# def Del(n, m):
#     return n % m == 0
#
#
# for A in range(1, 1000):
#     for x in range(1, 10000):
#         if (((Del(x, 24) and Del(x, 36)) <= Del(x, A)) and (A**2 - A - 5000<112)) == False:
#             break
#     else:
#         print(A)


# for A in range(1, 10000):
#     for x in range(1, 10000):
#         if ((x&75 == 0) or ((x&80==0) <= (x&A != 0))) == False:
#             break
#     else:
#         print(A)


# for A in range(0, 10000):
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             if ((x +2*y> A) or (x <=15) or (y<=30)) == False:
#                 break
#         if ((x +2*y> A) or (x <=15) or (y<=30)) == False:
#             break
#     else:
#         print(A)


# def Del(n, m):
#     return n % m == 0
#
#
# for A in range(1, 1000):
#     for x in range(1, 10000):
#         if ((Del(x, A) and Del(x, 7)) <= (not (Del(x, 7)) or Del(x, 311))) == False:
#             break
#     else:
#         print(A)


# def Tr(n, m, k):
#
#     return n +m > k and n+k > m and m +k > n
#
#
#
# for A in range(1, 1000):
#     for x in range(1, 10000):
#         if (not ((Tr(x, 11, 24) == (not (max(x, 7) > 32))) and (Tr(x, A, 7)))) == False:
#             break
#     else:
#         print(A)


def Ug(a, b, c):
    return (a + b + c) == 180


for A in range(1, 1000):
    for x in range(1, 10000):
        if (Ug(47, A, x + 40) == (Ug(A, x, 45) and (not (A + 30 < 156)))) == False:
            break
    else:
        print(A)
