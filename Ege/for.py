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


# def Ug(a, b, c):
#     return (a + b + c) == 180
#
#
# for A in range(1, 1000):
#     for x in range(1, 10000):
#         if (Ug(47, A, x + 40) == (Ug(A, x, 45) and (not (A + 30 < 156)))) == False:
#             break
#     else:
#         print(A)


# 27


# f = open("")
# n = int(f.readline())
# a = [int(s) for s in f]
# troyka = []
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         for j1 in range(j+1, len(a)):
#             troyka.append(a[i] * a[j] * a[j1])
# print(max(troyka))


# f = open("")
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i, n):
#         if sum(a[i:j + 1]) % 101 == 0:
#             res.append([sum(a[i:j +1]), (j+1) - i])
# res.sort(reverse=True)
# print(res[:5])


# f = [
#     835,
#     829,
#     947,
#     493,
#     53,
#     378,
#     207,
#     108,
#     271,
#     100,
#     451,
#     94,
#     712,
#     213,
#     363,
#     892,
#     299,
#     414,
#     235,
#     103]
# n = 20
# a = [int(s) for s in f]
# res = []
# cnt = 0
# for i in range(n):
#     for j in range(i, n):
#         if (a[i] + a[j]) % 12 == 0:
#             cnt += 1
# print(cnt)

# f = open("27dfuf")
# n = int(f.readline())
# a = [int(s) for s in f]
# k = 101
# res = []
# for i in range(n):
#     for j in range(i, n):
#         if sum(a[i:j +1])% 101 ==0:
#             res.append([sum(a[i:j +1]), (j+1) - i])
# res.sort(reverse=True)
# print(max(res))


# f = open("27dfuf")
# n, m = map(int, f.readline().split())
# a = [int(s) for s in f]
# res = []
# for i in range(m, n-m):
#     res.append(sum(a[i-m:i+m+1]))
# print(max(res))


# f = open("27dfuf")
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     cost = 0
#     for j in range(n):
#         cost += abs(j-i)*a[j]
#     res.append(cost)
# print(max(res))


# f = open("323")
# n = int(f.readline())
# a = [int(s) for s in f]
# cnt = 0
# for i in range(n):
#     for j in range(i +1, n):
#         if (a[i]+a[j]) % 12 == 0:
#             cnt += 1
# print(cnt)


# f = open("323")
# n = int(f.readline())
# a = [int(s) for s in f]
# k = 71
# res = []
# for i in range(n):
#     for j in range(i,n):
#         if sum(a[i:j + 1]) % k == 0:
#             res.append([sum(a[i:j + 1]), (j + 1) - i])
# res.sort(reverse=True)
# print(res[:5])


# def nech(a):
#     cnt= 0
#     for x in a:
#         if x % 2 == 0:
#             cnt +=1
#     return cnt

# f = open("656")
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i, n):
#         if nech(a[i:j+1]) % 22 ==0:
#             res.append(sum(a[i:j+1]))
# print(max(res))


# f = open("6")
# n, m = map(int, f.readline().split())
# a = [int(s) for s in f]
# res = []
# for i in range(m, n-m):
#     res.append(sum(a[i-m:i+m+1]))
# print(max(res))


# f = open("6")
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     cost = 0
#     for j in range(n):
#         cost += (abs(i - j) * a[j])
#     res.append(cost)
#
# print(max(res))


# Variant ege

# a = 49 ** 10 + 7 ** 30 - 49
# s = " "
# while a != 0:
#     s += str(a % 7)
#     a = a // 7
#
# s = s[::-1]
# print(s.count("6"))


# def Del(n, m):
#     return n % m == 0
#
#
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (not (Del(x, A)) <= (Del(x, 6) <= (not (Del(x, 4))))) == 1:
#             print(A)


# def F(n):
#     if n == 1:
#         return 0
#     if n > 1:
#         return F(n - 1) + n
#
#
# def G(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return G(n - 1) * n
#
#
# print(F(5) + G(5))


# f = open("17.txt")
# a = [int(s) for s in f]
# res = []
# for x in range(len(a)-1):
#     for y in range(x+1, len(a)):
#         if (a[x] * a[y]) % 10 == 0:
#             res.append(a[x] + a[y])
# print(len(res), max(res))


# f = open("28131_B.txt")
# n = int(f.readline())
# a = [int(s) for s in f]
# res = []
# for i in range(n):
#     for j in range(i, n):
#         if a[i] > a[j] and (a[i] + a[j]) % 120 == 0:
#             res.append([a[i] + a[j], a[i], a[j]])
# print(max(res))


# a = "8"* 1000
# while "999" in a or "888" in a:
#     if "888" in a:
#         a= a.replace("888", "9",1)
#     else:
#         a = a.replace("999", "8", 1)
# print(a)


# 19-21


# def WIN1(s):
#     return (s + 1) >= 100 or (s * 2) >= 100
#
#
# def LOSS1(s):
#     return (not(WIN1(s))) and WIN1(s+1) and WIN1(s*2)
#
# def WIN2(s):
#     return LOSS1(s+1) or LOSS1(s*2)
#
# def LOSS12(s):
#     return WIN2(s+1) and WIN1(s*2)
#
# for s in range(1,100):
#     if LOSS12(s):
#         print(s)


# 2
# 19a
# def WIN1(s):
#     return (s+1)>= 93 or (s*3-1) >= 93
#
# for s in range(1, 93):
#     if WIN1(s+1) or WIN1(s*3-1):
#         print(s)

# 20

# def WIN1(s):
#     return (s+1)>= 93 or (s*3-1) >= 93
#
# def LOSS1(s):
#     return (not(WIN1(s))) and WIN1(s+1) and WIN1(s*3-1)
#
# def WIN2(s):
#     return LOSS1(s+1) or LOSS1(3*s-1)
#
#
# for s in range(1, 93):
#     if WIN2(s):
#         print(s)


# 21

# def WIN1(s):
#     return (s + 1) >= 93 or (s * 3 - 1) >= 93
#
#
# def LOSS1(s):
#     return (not (WIN1(s))) and WIN1(s + 1) and WIN1(s * 3 - 1)
#
#
# def WIN2(s):
#     return LOSS1(s + 1) or LOSS1(3 * s - 1)
#
# def LOSS12(s):
#     return WIN2(s+1) and WIN1(s*2)
#
#
# for s in range(1, 93):
#     if LOSS12(s):
#         print(s)


# 22
# a
# def WIN1(x, s):
#     return (x + 2 + s) >= 156 or (x * 5 + s) >= 156
#
#
# x = 5
# for s in range(1, 150):
#     if WIN1(x, s):
#         print(s)


# b

# def WIN1(x, s):
#     return (x + 2 + s) >= 156 or (x * 5 + s) >= 156 or (x + 5 * s) >= 156
#
#
# x = 5
# for s in range(1, 150):
#     if WIN1(x + 2, s) or WIN1(x, s + 2) or WIN1(x * 5, s) or WIN1(x, s * 5):
#         print(s)


# 22 (20)

# def WIN1(x, s):
#     return (x + 2 + s) >= 156 or (x * 5 + s) >= 156 or (x + 5 * s) >= 156
#
#
# def LOSS1(x, s):
#     return (not (WIN1(s))) and WIN1(x + 2, s) and WIN1(x, s + 2) and WIN1(x * 5, s) and WIN1(x, s * 5)
#
#
# def WIN2(x, s):
#     return LOSS1(x + 2, s) or LOSS1(x, s + 2) or LOSS1(x * 5, s) or LOSS1(x, s * 5)
#
#
# x = 5
# for s in range(1, 150):
#     if WIN2(x, s):
#         print(s)


# 21

# def WIN1(x, s):
#     return (x + 2 + s) >= 156 or (x * 5 + s) >= 156 or (x + 5 * s) >= 156
#
#
# def LOSS1(x, s):
#     return (not (WIN1(x, s))) and WIN1(x + 2, s) and WIN1(x, s + 2) and WIN1(x * 5, s) and WIN1(x, s * 5)
#
#
# def WIN2(x, s):
#     return LOSS1(x + 2, s) or LOSS1(x, s + 2) or LOSS1(x * 5, s) or LOSS1(x, s * 5)
#
#
# def LOSS12(x, s):
#     return (WIN1(x + 2, s) or WIN2(x + 2, s)) and (WIN1(x, s + 2) or WIN2(x, s + 2)) \
#         and (WIN1(x * 5, s) or WIN2(x * 5, s)) and (WIN1(x, s * 5) or WIN1(x, s * 5)) \
#         and (WIN2(x + 2, s) or WIN2(x, s + 2) or WIN2(x * 5, s) or WIN2(x, s * 5))
#
#
# x = 5
# for s in range(1, 150):
#     if LOSS12(x, s):
#         print(s)


# Разбор варианта
# print("x", "y", "z", "w", "F")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((y <= x) and w and (not (z))):
#                     print(x, y, z, w)

#
# for n in range(1, 100):
#     a = bin(n)[2:]
#     if n % 3 == 0:
#         a += a[-3:]
#     if n % 3 != 0:
#         a += bin((n % 3) * 3)[2:]
#     r = int(a, 2)
#     if r >= 76:
#         print(n)


# from turtle import *
# screensize(2000, 2000)
# k = 20
# tracer(0)
# left(90)
# pendown()
# for i in range(4):
#     forward(20 *k)
#     right(270)
# penup()
# forward(6 *k)
# right(270)
# forward(10 *k)
# right(90)
# pendown()
# for i in range(2):
#     forward(20 * k)
#     right(270)
#     forward(24 * k)
#     right(270)
# penup()
# for x in range(-40, 10):
#     for y in range(-10, 40):
#         setpos(x*k, y*k)
#         dot()
# done()
# print(21*25 + 21*21 - 11*15)


# from itertools import *
#
# cnt = 0
# for i in product("012345678", repeat=5):
#     numb = "".join(i)
#     if numb.count("3") == 2 and numb[0] != 0 and \
#             all(("2" + nech not in numb) and (nech + "2" not in numb) for nech in "1357"):
#         cnt += 1
# print(cnt)


# f = open("9")
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     if len(povt) == 2 and sum(povt) / len(povt) < sum(ne_povt) / len(ne_povt):
#         cnt += 1
# print(cnt)

# s = []
# for n in range(4, 10000):
#     a = "1" + "2" * n
#     while "12" in a or "322" in a or "222" in a:
#         if "12" in a:
#             a = a.replace("12", "2", 1)
#         if "322" in a:
#             a = a.replace("322", "21", 1)
#         if "222" in a:
#             a = a.replace("222", "3", 1)
#     s.append(sum(map(int, a)))
# print(max(s))


# from string import *
# for x in "0123456789ABCDEFGHIJK":
#     if (int(f"63{x}59685", 22) + int(f"17{x}53", 22) + int(f"36{x}5", 22)) % 21 ==0:
#         print(x, (int(f"63{x}59685", 22) + int(f"17{x}53", 22) + int(f"36{x}5", 22)) // 21)


# for A in range(0, 1000):
#
#     if all((48 != y + 2 * x) or (A > x) or (A > y) for x in range(0, 1000) for y in range(0, 1000)):
#         print(A)
#         break


# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n - 1 + F(n - 1)
#
#
# print(F(2028) - F(2024))


# f = open("17")
# a = [int(s) for s in f]
# max22 = max([x for x in a if str(x)[-2:] == "22"])
# sum_troyki = []
# for i in range(len(a) -2):
#     if ((len(str(abs(a[i]))) == 5) + (len(str(abs(a[i+1]))) ==5) + (len(str(abs(a[i+2]))) ==5)) == 2 and \
#             (a[i] +a[i+1] + a[i+2]) <= max22:
#         sum_troyki.append(a[i] + a[i+1] +a[i+2])
# print(len(sum_troyki), max(sum_troyki))


def WIN1(s):
    return (s + 1) >= 184 or (s + 5) >= 184 or (s * 4) >= 184


def LOSS1(s):
    return not WIN1(s) and (s + 1)

    # 26


# f = open("")
# n, k = map(int, f.readline().split())
# a = [int(s) for s in f]
# a.sort(reverse=True)
# print(a[:87])
# print(a[87:174])
# print(sum(a[:87]) / len(a[:87]))


# f = open("")
# s, n = map(int, f.readline().split())
# a = [int(s) for s in f]
# a.sort()
# print(sum(a[:4413]))
# print(len(a[:4413]))
# print(s- sum(a[:4412]))
# print(56 in a)


# f = open("")
# s, n = map(int, f.readline().split())
# a = [int(s) for s in f]
# a.sort()
# product = []
# for x in a:
#     if sum(product) + x <= s:
#         product.append(x)
#     elif sum(product[:-1]) + x <= s:
#         del product[-1]
#         product.append(x)
#     else:
#         break
# print(len(product), max(product))


# f = open("")
# s, n = map(int, f.readline().split())
# a = [int(s) for s in f]
# a.sort()
# product = []
# cnt_neok= 0
# for x in a:
#     if sum(product) + x <= s:
#         product.append(x)
#     elif sum(product[:-1]) + x <= s:
#         del product[-1]
#         product.append(x)
#     else:
#         cnt_neok += 1
# print(len(product), max(product))
# print(len(product), cnt_neok)


# f = open("")
# n = int(f.readline())
# a = [int(s) for s in f]
# a.sort()
# a120 = [x for x in a if x > 120]
# print(len(a120))
# print(len(a120) // 2)
# sale = (sum(a120[:len(a120) // 2]) * 0.25)
# print(n - sale)


# f = open("")
# n = int(f.readline())
# a = [int(s) for s in f]
# a.sort(reverse=True)
# sale1 = sum(a[:len(a) // 3])
# print(sum(a) - sale1)
# for i in range(n):
#     if (i+1) % 3 == 0:
#         a[i] = 0
# print(sum(a))


# f = open("26")
# k, n = map(int, f.readline().split())
# a = [int(s) for s in f]
# a.sort()
# product = []
# for x in a:
#     if sum(product) + x <= k:
#         product.append(x)
#     elif sum(product[:-1]) + x <= k:
#         del product[-1]
#         product.append(x)
#     else:
#         break
# print(len(product), max(product))


# f = open("26")
# k, n = map(int, f.readline().split())
# a = [int(s) for s in f]
# a.sort()
# product = []
# cnt_neok = 0
# for x in a:
#     if sum(product) <= k:
#         product.append(x)
#     elif sum(product[:-1]) + x <= k:
#         del product[-1]
#         product.append(x)
#     else:
#         cnt_neok +=1
# print(len(product), cnt_neok)


# f = open("26")
# n = int(f.readline())
# a = [int(s) for s in f]
# a.sort()
# a120 = [x for x in a if x > 120]
# sale = sum(a120[:len(a120) // 2]) * 0.25
# print(sum(a) - sale, max(a120[:len(a120) // 2]))


# f = open("26.1")
# n = int(f.readline())
# a = [int(s) for s in f]
# a.sort(reverse=True)
# sale1 = (sum(a[:len(a) // 3]))
# print(sum(a) - sale1)
# for i in range(n):
#     if (i + 1) % 3 == 0:
#         a[i] = 0
# print(sum(a))


# f = open("26.1")
# n = int(f.readline())
# a = [int(s) for s in f]
# a.sort(reverse=True)
# gift = []
# for box in boxes:
#     if gift == []  # len(gift) == 0:
#         gift.append(box)
#     elif gift[-1] - box >= 3:
#         gift.append(box)
# print(len(gift), min(gift))


# f = open("26.1")
# n = int(f.readline())
# boxes = [int(s) for s in f]
# boxes.sort(reverse=True)
# blocks = []
# while boxes != []:
#     gift = [boxes[0]]
#     del boxes[0]
#     for box in boxes[:]:
#         if gift[-1] - box >= 5:
#             gift.append(box)
#             boxes.remove(box)
#     blocks.append(gift)
# print(len(blocks), len(blocks[0]))


# f = open("26.1")
# n = int(f.readline())
# boxes = []
# for s in f:
#     lens, color = s.split()
#     boxes.append([int(lens), color])
# boxes.sort(reverse=True)
# blocks = []
# while boxes != []:
#     gift = [boxes[0]]
#     del boxes[0]
#     for box in boxes[:]:
#         if gift[-1][0] - box[0] >= 8 and gift[-1][1] != box[1]:
#             gift.append(box)
#             boxes.remove(box)
#     blocks.append(gift)
# print(len(blocks), len(blocks[0]), len(max(blocks, key=len)))


# f = open("26.1")
# k = int(f.readline())
# n = int(f.readline())
# files = []
# cnt = 0
# last_disk = 0
# for s in f:
#     start, end = map(int, s.split())
#     files.append([start, end])
# files.sort()
# disk = [0] * k
# for start, end in files:
#     for i in range(k):
#         if start > disk[i]:
#             disk[i] = end
#             cnt += 1
#             last_disk = (i + 1)
#             break
# print(cnt, last_disk)


# f = open("")
# n = int(f.readline())
# start_lenta = []
# end_lenta = []
# for i in range(n):
#     shlif, okr = map(int, f.readline().split())
#     if shlif < okr:
#         start_lenta.append([shlif, i + 1])
#     if okr > shlif:
#         end_lenta.append([okr, i + 1])
# start_lenta.sort()
# end_lenta.sort()
# print(max(start_lenta), max(end_lenta))
# print(len(start_lenta) - 1)


# f = open("")
# n = int(f.readline())
# data = []
# for s in f:
#     start, end = map(int, s.split())
#     data.append([end, start])
# data.sort()
# zal = 0
# podoshel = []
# for end, start in data:
#     if start >= zal:
#         zal = end
#         podoshel.append([start, end])
#     if start >= 1379:
#         print(start, end)
# print(len(podoshel), podoshel)


# f = open("")
# n = int(f.readline())
# data = []
# for s in f:
#     ryad, mesto = map(int, s.split())
#     if [ryad, mesto] not in data:
#         data.append([ryad, mesto])
# data.sort()
# cur = 1
# for i in range(1, len(data)):
#     if (data[i][0] == data[i - 1][0]) and \
#             (data[i][1] - data[i - 1][1]) == 1:
#         cur += 1
#         print(cur, data[i])
#     else:
#         cur = 1


# f = open("26")
# n = int(f.readline())
# data = []
# for s in f:
#     ryad, mesto = map(int, s.split())
#     data.append([ryad, mesto])
# data.sort()
# for i in range(1, len(data)):
#     if (data[i][0] == data[i-1][0]) and (data[i][1] - data[i-1][1]) == 4:
#         print(data[i], data[i-1])


# 9, 15, 4

# def to_base5(x):
#     s = ""
#     while x > 0:
#         s += str(x % 5)
#         x = x // 5
#     return s[::-1]
#
#
# a = []
# for n in range(1, 10000):
#     n5 = to_base5(n)
#     if n % 7 == 0:
#         n5 = n5[:4] + n5 + "0" * (4 - len(n5)) + n5[-4:]
#     else:
#         n5 += bin((n % 7) * 2)[2:]
#     r = int(n5, 5)
#     if r > 1000 and r % 760 == 0:
#         a.append(r)
# print(min(a))


# def is_prostoe(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return x > 1
#
#
# from math import prod
#
# f = open("17")
# a = [int(s) for s in f]
# pyaterki = []
# for i in range(len(a) - 4):
#     if sum([1 for x in a[i:i + 5] if is_prostoe(x)]) == 2 and \
#             sum([1 for x in a[i: i + 5] if x ** 0.5 % 1 == 0]) >= 3:
#         pr = prod(a[i:i + 5])
#         pyaterki.append(sum(map(int, str(pr))))
# print(len(pyaterki), max(pyaterki))


# def tr(x):
#     s = ""
#     while x > 0:
#         s += str(x % 3)
#         x = x // 3
#     return s[::-1]
#
#
# for n in range(1, 10000):
#     n3 = tr(n)
#     if n % 3 == 0:
#         n3 = n3 + n3[-3:]
#     else:
#         n3 = n3 + tr((n % 3) * 3)
#     r = int(n3, 3)
#     if r > 344:
#         print(n)
#         break

# from string import *
#
# alph = "0123456789ABCDEFGHIJ"
# for x in alph:
#     if (int(f"13{x}CF", 20) + int(f"47GH{x}", 20)) % 19 == 0:
#         print((int(f"13{x}CF", 20) + int(f"47GH{x}", 20)) // 19)


# a = hex(16 ** 161 - 16 ** 61 - 16 ** 6)[2:]
# print(a)
# cnt = 0
# for i in a:
#     if "f" in str(a):
#         cnt += 1
# print(cnt)


# def to_base_39(number):
#     characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabc"
#
#     base = 39
#
#     result = ""
#
#     while number > 0:
#         remainder = number % base
#
#         result = characters[remainder] + result
#
#         number //= base
#
#     return result
#
#
# def from_base_39(number):
#     characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabc"
#
#     base = 39
#
#     result = 0
#
#     for i, char in enumerate(reversed(number)):
#         value = characters.index(char)
#
#         result += value * (base ** i)
#
#     return result
#
#
# def R(n):
#     n1 = str(to_base_39(n))
#
#     if n % 13 == 0:
#         n1 = "222" + n1 + "32F"
#
#     else:
#         n1 += to_base_39((n % 123) * 58)
#
#     return from_base_39(n1)
#
#
# for i in range(1, 100000):
#
#     if R(i) < 100_000:
#         print(i, R(i))


# alph = "0123456789ABCD"
# for x in alph:
#     for y in alph:
#         if (int(f"ABCD3{y}2{x}1", 14) + int(f"192{x}9", 14)) % 107 == 0:
#             print((int(f"ABCD3{y}2{x}1", 14) + int(f"192{x}9", 14)) // 107)

# from string import *
#
# alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:23]
# for x in alph:
#     for y in alph:
#         if (int(f"13{y}{x}9", 23) + int(f"22{y}22", 23)) % 2 == 0:
#             y = 6
#             print((int(f"13{y}{x}9", 23) + int(f"22{y}22", 23)) // 18)


# f = open("26")
# a = [int(s) for s in f]
# min_el = min([i for i in a if str(abs(i))[-3:] == "600"])
# troy = []
# for i in range(len(a) - 2):
#     if (int((len(str(abs(a[i]))) == 5)) + int((len(str(abs(a[i + 1])))== 5)) + int((len(str(abs(a[i + 2]))) == 5))) <= 2\
#             and (a[i] + a[i + 1] + a[i + 2]) >= min_el:
#         troy.append(a[i] + a[i + 1] + a[i + 2])
# print(len(troy), min(troy))


# f = open("26")
# a = [int(s) for s in f]
# max_el = max([x for x in a if str(x)[-2:] == "11"])
# res = []
# for i in range(len(a) - 1):
#     if str(oct(a[i]))[-1] == str(oct(a[i + 1]))[-1] and \
#             ((a[i] % 5 == 0 and a[i + 1] % 7 == 0 and a[i] % 35 !=0 and a[i+1] % 35 !=0)
#              or (a[i + 1] % 5 == 0 and a[i] % 7 == 0 and a[i] % 35 !=0 and a[i+1] % 35 !=0)) and \
#             (a[i] ** 2 + a[i + 1] ** 2) <= max_el ** 2:
#         res.append(a[i] + a[i + 1])
# print(len(res), min(res))


# print("x y z w F")
# for F in range(2):
#     for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 for w in range(2):
#                     if (((y <= x) == (w <= (not (z)))) and (w or x)) == F:
#                         print(x, y, z, w, F)


# for n in range(1, 1000):
#     n2 = bin(n)[2:]
#     if n2.count("1") % 2 == 0:
#         n22 = n2[2:]
#         n22 = "10" + n22 + "0"
#
#     else:
#         n22 = n2[2:]
#         n22 = "11" + n22 + "1"
#
#     r = int(n22, 2)
#     if r >= 26:
#         print(n)

# from turtle import *
# k = 10
# left(90)
# pendown()
# right(90)
# for i in range(3):
#     right(45)
#     forward(15*k)
#     right(45)
# right(315)
# forward(15*k)
# for i in range(2):
#     right(90)
#     forward(15*k)
# penup()
# for x in range(50*k, -50*k, k):
#     for y in range(50*k, -50*k, k):
#         goto(x*k,y*k)
#         dot(3)
# done()


# f = open("9")
# a = [int(s) for s in f]
# for i in range(len(a) - 6):
#     if a[i]


# a = "2" * 2022 + "4" * 2023
# while "222" in a:
#     a.replace("222", "3", 1)
#     a.replace("333", "4", 1)
#     a.replace("444", "2", 1)
# print(a)

# from string import *
# alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:16]
# for x in alph:
#     if (int(f"D49{x}1", 16) + int(f"48A3{x}", 16)) % 14 == 0:
#         print((int(f"D49{x}1", 16) + int(f"48A3{x}", 16)) // 14)


# def Del(n, m):
#     return n % m == 0
#
#
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((Del(x, 2) <= (not (Del(x, 5)))) or (x + A >= 90)) == 1:
#             print(A)


# def Del(n, m):
#     return n % m == 0
#
#
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if (not (Del(x, A)) <= (Del(x, 6) <= (not (Del(x, 4))))) == 1:
#             print(A)


# def F(n):
#     if n < 3:
#         return 1
#     if n > 2 and n % 2 == 0:
#         return F(n - 1) + n - 1
#     if n > 2 and n % 2 != 0:
#         return F(n - 2) + 2 * n - 2
#
#
# print(F(31))


# f = open("17")
# a = [int(s) for s in f]
# para = []
# min_el = min([x for x in a if x % 6 == 0])
# for i in range(len(a) - 1):
#     if a[i] % min_el == 0 and a[i+1] % min_el == 0:
#         para.append(a[i] + a[i+1])
# print(len(para), max(para))


# def task(start, end):
#     if start > end:
#         return 0
#     if start == end:
#         return 1
#     if start < end:
#         return task(start + 2, end) + task(start * 2, end)
#
#
# print(task(1, 24) * task(24, 50))

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


# f = open("24")
# a = [s for s in f]
# cnt = 0
# if "BA" in a:
#     cnt += 1
# print(cnt)
# # or "DA" in a or "BADA" in a


# f = open("10")
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#
#     if len(povt) == 2:
#         if all(x % 2 != 0 for x in povt) and all(x % 2 == 0 for x in ne_povt):
#             cnt += 1
#
# print(cnt)


# from math import prod
# f = open('10')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x)== 1]
#     if len(povt) == 2:
#         pr = prod(povt)
#         pr2 = sum(map(int, str(pr)))
#         if str(oct(pr2**2))[-1] == "0":
#             cnt += 1
# print(cnt)


# f = open("10")
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     ne_povt = [x for x in a if a.count(x) == 1]
#     min_el = min([x for x in a])
#     if len(povt) == 4:
#         if min_el in povt:
#             cnt += 1
# print(cnt)


# f = open("266")
# n = int(f.readline())
# data = []
#
# for s in f:
#     ryad, mesto = map(int, s.split())
#     if [ryad, mesto] not in data:
#         data.append([ryad, mesto])
# data.sort()
# cnt = 1
# for i in range(1, len(data)-3):
#     if (data[i][0] == data[i - 1][0]) and (data[i][1] - data[i - 1][1]) == 4:
#         cnt += 1
#         print(cnt, data[i])
#     else:
#         cnt = 1


# f = open("")
# n = int(f.readline())
# data = []
# for s in f:
#     ryad, mesto = map(int, s.split())
#     if [ryad, mesto] not in data:
#         data.append([ryad, mesto])
# data.sort()
# cur = 1
# for i in range(1, len(data)):
#     if (data[i][0] == data[i - 1][0]) and \
#             (data[i][1] - data[i - 1][1]) == 1:
#         cur += 1
#         print(cur, data[i])
#     else:
#         cur = 1


# f = open("266")
# n = int(f.readline())
# data = []
# cur = 1
# for s in f:
#     ryad, mesto = map(int, s.split())
#     if [ryad, mesto] not in data:
#         data.append([ryad, mesto])
# data.sort()
# for i in range(1, len(data)):
#     if (data[i][0] == data[i - 1][0]) and (data[i][1] - data[i - 1][1]) == 6:
#         cur += 1
#         print(cur, data[i])
#     else:
#         cur = 1


# f = open("266")
# n = int(f.readline())
# data = []
# for s in f:
#     start, end = map(int, s.split())
#     data.append([end, start])
# data.sort()
# zal = 0
# podoshel = []
# for end, start in data:
#     if start >= zal:
#         zal = end
#         podoshel.append([start, end])
#     if start >= 1338:
#         print(start, end)
# print(len(podoshel))


# f = open("")
# n = int(f.readline())
# data = []
# for s in f:
#     start, end = map(int, s.split())
#     data.append([end, start])
# data.sort()
# zal = 0
# podoshel = []
# for end, start in data:
#     if start >= zal:
#         zal = end
#         podoshel.append([start, end])
#     if start >= 1379:
#         print(start, end)
# print(len(podoshel), podoshel)


# f = open("266")
# n = int(f.readline())
# start = []
# end = []
# for i in range(n):
#     shlif, okr = map(int, f.readline().split())
#
#     if shlif < okr:
#         start.append([shlif, i +1])
#     if shlif > okr:
#         end.append([okr, i +1])
# print(max(start), max(end))
# print(len(start))


# f = open("")
# n = int(f.readline())
# start_lenta = []
# end_lenta = []
# for i in range(n):
#     shlif, okr = map(int, f.readline().split())
#     if shlif < okr:
#         start_lenta.append([shlif, i + 1])
#     if okr > shlif:
#         end_lenta.append([okr, i + 1])
# start_lenta.sort()
# end_lenta.sort()
# print(max(start_lenta), max(end_lenta))
# print(len(start_lenta) - 1)
#
#


# 25

# from fnmatch import *
# for x in range(0, 10**8, 61):
#     if fnmatch(str(x), "23456??8"):
#         print(x, x // 61)


# from fnmatch import *
#
# for x in range(0, 10 ** 8, 63):
#     if fnmatch(str(x), "134?3?"):
#         print(x, x // 63)


# from fnmatch import *
# a = []
# for x in range(0, 10**8, 2023):
#     if fnmatch(str(x), "37*87?"):
#         a.append([x, x // 2023])
# a.sort()
# print(a)


# from re import *
# for x in range(0, 10**8, 123):
#     if fullmatch(r"154\d8\d", str(x)):
#         print(x, x // 123)


# from re import *
# for x in range(0, 10**8, 193):
#     if fullmatch(r"64\d*32\d2", str(x)):
#         print(x, x // 193)


# for x in range(123456, 123487+1):
#     deliteli = []
#     for d in range(1, x +1):
#         if x % d ==0:
#             deliteli.append(d)
#     if len(deliteli) == 6:
#         print(deliteli)


# for x in range(15545, 15844 + 1):
#     deliteli = []
#     for d in range(2, x):
#         if x % d == 0:
#             deliteli.append(d)
#     if len(deliteli) == 5:
#         print(x, max(deliteli))


# for x in range(950000, 950000+100000):
#     F = 0
#     deliteli = []
#     for d in range(2, x):
#         if x % d == 0:
#             deliteli.append(d)
#     if deliteli:
#         F = max(deliteli) - min(deliteli)
#         if F !=0 and F % 13 == 0:
#             print(x, F)

# cnt = 0
# for x in range(800001, 800001 + 10000):
#     for d in range(111, x, 100):
#         if x % d == 0 and str(d)[-2:] == "11":
#             print(x, d)
#             cnt += 1
#     if cnt == 5:
#         break


# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return n > 1
#
# for x in range(1_000_001, 1_000_001 +10_000):
#     deliteli = []
#     for d in range(2, x):
#         if x % d == 0:
#             deliteli.append(d)
#     if deliteli and is_prime(max(deliteli)):
#         print(x, max(deliteli))


# for x in range(800_001, 800_001 + 1000):
#     F = 0
#     deliteli = []
#     for d in range(2, x):
#         if x % d == 0:
#             deliteli.append(d)
#
#     if deliteli:
#         deliteli.sort()
#         F = deliteli[0] * deliteli[-2]
#
#     if F != 0 and F % (deliteli[0] + deliteli[1]) == 0:
#         print(x, F)


# f = open("")
# s = f.readline()
# a = s.split("R")
# print(len(max(a, key=len)))


# f = open("")
# s = f.readline()
# s = s.replace("U", "A")
# s = s.replace("T", "R")
# s = s.replace("S", "R")
# for i in range(100):
#     if "AR" * i in s:
#         print(i)



# f = open("")
# s = f.readline()
# s = s.replace("FGN", "*")
# s = s.replace("GFN", "*")
# for i in range(100):
#     if "*" * i in s:
#         print(i)


# f = open("")
# s = f.readline()
# s = s.replace("FJW", "FJ JW")
# s = s.replace("FJ", "JW")
# for i in range(100):
#     if "JW" * i in s:
#         print(i)




