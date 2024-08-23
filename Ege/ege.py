# 8
# cnt = 0
# n = 600001
# while cnt !=5:
#     for i in range(17, n, 10):
#         if n % i ==0:
#             print(n, i)
#             cnt+=1
#             break
#     n +=1

# 15
# def Del(n, m):
#     return n % m ==0
#
# for A in range(1, 1000):
#     for x in range(1, 1000):
#         if ((Del(x,2) <= (not(Del(x, 5)))) or (x + A >=70)) == 0:
#             break
#     else:
#         print(A)

# 23
# def task23(start, end):
#     if start < end:
#         return 0
#     if start == end:
#         return 1
#     return task23(start -2, end) + task23(start//2, end)
# print(task23(30, 14)*task23(14, 1))

# 9
# f = open("9")
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     nepovt = [x for x in a if a.count(x) == 1]
#     a.sort()
#     if a[-1] < (a[0] + a[1] + a[2]) and len(set(a)) == 4:
#         cnt += 1
# print(cnt)

# 9
# f = open("9")
# cnt =0
# for s in f:
#     a = list(map(int, s.split()))
#     if len(set(a)) == 4 and max(a) < (sum(a) - max(a)):
#         cnt +=1
# print(cnt)

# 16
# f = [0]*3000
# for n in range(1, 2500):
#     if n ==1:
#         f[n] = 1
#     if n >1:
#         f[n] = 2 *n * f[n-1]
# print((f[2024] - 4*f[2023]) / f[2022])


# 19
# def WIN1(s):
#     return (s+1) >=69 or (s*2)>=69
#
# def LOSS(s):
#     return (not(WIN1(s))) and WIN1(s+1) and WIN1(s*2)
#
# for s in range(1, 69):
#     if LOSS(s):
#         print(s)


# def WIN1(s):
#     return (s+1) >=69 or (s*2)>=69
#
# def LOSS(s):
#     return (not(WIN1(s))) and WIN1(s+1) and WIN1(s*2)
#
# def WIN2(s):
#     return LOSS(s+1) or LOSS(s*2)
#
# for s in range(1, 69):
#     if WIN2(s):
#         print(s)


# def WIN1(s):
#     return (s + 1) >= 69 or (s * 2) >= 69
#
#
# def LOSS(s):
#     return (not (WIN1(s))) and WIN1(s + 1) and WIN1(s * 2)
#
#
# def WIN2(s):
#     return LOSS(s + 1) or LOSS(s * 2)
#
#
# def LOSS12(s):
#     return ((WIN1(s + 1) or WIN2(s + 1)) and (WIN1(s * 2) or WIN2(s * 2)) and (WIN2(s + 1) or WIN2(s * 2)))
#
#
# for s in range(1, 69):
#     if LOSS12(s):
#         print(s)


# cnt = 0
# n = 600001
# while cnt !=5:
#     for i in range(17, n, 10):
#         if n % i ==0:
#             cnt +=1
#             print(n, i)
#             break
#     n +=1


# 17
# f = open("17")
# a = [int(s) for s in f]
# pari = []
# for i in range(len(a) -1):
#     if ((a[i]%18) + (a[i+1]%18)) == min(a):
#         pari.append(a[i] + a[i+1])
# print(len(pari), max(pari))

# def tr(n):
#     s = ""
#     while n > 0:
#         s += str(n%3)
#         n = n //3
#     return s[::-1]
#
# for x in range(1, 2031):
#     n = 3 **100 - x
#     n3 = tr(n)
#     if n3.count("0") == 2:
#         print(x)
#         break


# 8
# cnt =0
# from itertools import *
# for i in product("EILMS", repeat = 4):
#     x = "".join(i)
#     cnt +=1
#     if "LIME" in x:
#         print(cnt)


# cnt =0
# from itertools import *
# for i in product("AINRT", repeat = 5):
#     x = "".join(i)
#     cnt +=1
#     if cnt == 400:
#         print(x)


# from itertools import *
#
# cnt = 0
# for i in product("0123456", repeat=6):
#     x = "".join(i)
#     if x[0] != 0 and x.count("5") == 2:
#         if all(f"{k}5" not in x and f"5{k}"not in x for k in "0246"):
#             cnt += 1
# print(cnt)

# cnt =0
# from itertools import *
# for x in permutations("ГЕЛИЙ", r=5):
#     s = "".join(x)
#     if s[0]!= "Й" and "ИЕЙ" not in s:
#         cnt+=1
# print(cnt)

# 14
# s = 6542 ** 324 - 3560 ** 67 + 730 ** 12 - 510
# cnt = 0
# while s > 0:
#     if s % 3 == 2:
#         cnt += 1
#     s = s // 3
# print(cnt)

# alph = "0123456789ABCDEF"
# for x in alph:
#     if (int(f"{x}432", 16) + int(f"234{x}", 16)) % 15 == 0:
#         print(x, (int(f"{x}432", 16) + int(f"234{x}", 16)) / 15)


# 17
# f = open("177")
# a = [int(s) for s in f]
# pari = []
# for i in range(len(a) - 1):
#     if ((a[i] % 123) == min(a) or (a[i + 1] % 123) == min(a)):
#         pari.append(a[i] + a[i + 1])
# print(len(pari), max(pari))

# f = open("1777")
# a = [int(s) for s in f]
# pari = []
# n6 = [x for x in a if x % 10 == 6]
# for i in range(len(a) - 1):
#     if (a[i] in n6 and a[i + 1] not in n6) and (a[i] not in n6 and a[i + 1] in n6) and\
#             (a[i] ** 2 + a[i + 1] ** 2) < max(n6) ** 2:
#         pari.append(a[i] + a[i + 1])
# print(pari)


# f = open("177")
# a = [int(s) for s in f]
# troy = []
# n13 = max([x for x in a if str(abs(x))[-2:] == "13"])
# for i in range(len(a) - 2):
#     if ((len(str(abs(a[i]))) == 5) + (len(str(abs(a[i]))) == 5) + (len(str(abs(a[i]))) == 5)) == 2 and \
#             (a[i] + a[i + 1] + a[i + 2]) <= n13:
#         troy.append(a[i] + a[i + 1] + a[i + 2])
# print(len(troy), max(troy))


# 9
# f = open("99")
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     nep = [x for x in a if a.count(x) == 1]
#     if len(set(a))==5 and (max(nep) + min(nep)) <= sum(povt):
#         cnt += 1
# print(cnt)

# f = open("99")
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     nep = [x for x in a if a.count(x) == 1]
#     if len(povt)== 4 and (sum(povt) / len(povt)) >= (sum(nep) / len(nep)):
#         cnt += 1
# print(cnt)


# f = open("9")
# cnt = 0
# for s in f:
#     a = list(map(int, s.split()))
#     a.sort()
#     if (a[0] * a[3] == a[1] * a[2]) and max(a) ** 2 <= (max(a) * min(a)):
#         cnt += 1
# print(cnt)


# f = open("99")
# cnt =0
# for s in f:
#     a = list(map(int, s.split()))
#     povt = [x for x in a if a.count(x) > 1]
#     nep = [ x for x in a if a.count(x) ==1]
#     if len(povt)==2:
#         if all(x%2 !=0 for x in povt) and all(x%2==0 for x in nep):
#             cnt +=1
# print(cnt)

# 8
# from itertools import *
# cnt =0
# for i in product("0123456789AB", repeat=6):
#     x = "".join(i)
#     if x[0] !="0" and x.count("7")==1 and (x.count("A") + x.count("B"))<=3:
#         cnt +=1
# print(cnt)

# 17
# f = open("17")
# a = [int(s) for s in f]
# n32 = [x for x in a if str(abs(x))[-2:] == "32"]
# otr = [x for x in a if str(x)[0] == "-"]
# pari = []
# for i in range(len(a) - 1):
#     if (a[i] in otr or a[i + 1] in otr) and (a[i] + a[i + 1]) < len(n32):
#         pari.append(a[i] + a[i + 1])
# print(len(pari), max(pari))

# 14
# for x in range(1, 2031):
#     s = 3**100 - x
#     s3 = ""
#     while s > 0:
#         s3 += str(s % 3)
#         s = s // 3
#     if s3.count("0") == 2:
#         print(x)
#         break


# intttttttttt

# 10101010.10011011.10001001.10110101
# 11111111.11111111.11111110
# 10101010.10011011.10001000.00000000


# 15
# def Del(n,m):
#     return  n %m ==0
# B = list(range(70,91))
# for A in range(1, 10000):
#     for x in range(1, 10000):
#         if (Del(x, A) or ((x in B) <= (not(Del(x, 27))))) ==0:
#             break
#     else:
#         print(A)


# 13
# from ipaddress import *
# cnt = 0
# ip_net = ip_network("106.184.0.0/255.255.240.0")
# for ip_ad in ip_net:
#     if f"{ip_ad:b}".count("1")%3 ==0:
#         cnt +=1
# print(cnt)

# 16
# f = [0]* 2500
# for n in range(1, 2500):
#     if n ==1:
#         f[n] = 1
#     if n >1:
#         f[n] = 2 *n * f[n-1]
# print((f[2024] - 4*f[2023]) / f[2022])

# 8
# from itertools import *
# cnt = 1
# for i in product(sorted("ФОКУС"), repeat = 5):
#     x = "".join(i)
#     if x.count("Ф")==0 and x.count("У")==2:
#         print(cnt)
#     cnt +=1


# 14
# def cem(n):
#     s = ""
#     while n > 0:
#         s += str(n % 7)
#         n = n // 7
#     return s[::-1]
#
#
# for x in range(1, 2031):
#     s = 7 ** 218 + 7 ** 150 - x
#     if cem(s).count("0") == 70:
#         print(x)
#         break


# 25
# n = 600001
# cnt = 0
# while cnt !=5:
#     for i in range(17, n, 10):
#         if n % i ==0:
#             cnt +=1
#             print(n, i)
#             break
#     n +=1

# 25
# n = 700001
# cnt = 0
# while cnt != 5:
#     M = 0
#     for i in range(2, n):
#         if n % i == 0:
#             M = i + n // i
#             break
#     if str(M)[-1] == "4":
#         cnt +=1
#         print(n, M)
#
#     n += 1


# 14
# def tr(n):
#     s = ""
#     while n >0:
#         s += str(n %3)
#         n = n // 3
#     return s[::-1]
# res = []
# for x in range(1, 2031):
#     s = tr(3**100 -x)
#     for n in range(len(s), 0 , -1):
#         if s.count("0") == n:
#             res.append([n , x])
# res.sort(reverse=True)
# print(res[:10])


# 9
# f = open("9")
# cnt =0
# for s in f:
#     a = list(map(int, s.split()))
#     nepov = [x for x in a if a.count(x)==1]
#     povt = [x for x in a if a.count(x) >1]
#     if len(povt) ==3 and povt[0] >= (sum(nepov)/len(nepov)):
#         cnt +=1
# print(cnt)


# 25
# for n in range(123456, 123488):
#     deli = []
#     for d in range(1, 123488):
#         if n % d ==0:
#             deli.append(d)
#     if len(deli)==6:
#         print(deli)

# 25
# for n in range(15545, 15845):
#     deli = []
#     for i in range(2, n):
#         if n % i ==0:
#             deli.append(i)
#     if len(deli)==5:
#         print(n, max(deli))


# 25
# n = 950001
# cnt = 0
# while cnt != 5:
#     F = 0
#
#     for d in range(2, n):
#         if n % d == 0:
#             F = n // d - d
#             break
#     if F != 0 and F % 13 == 0:
#         cnt +=1
#         print(n, F)
#
#     n +=1


# 25
# n = 800001
# cnt =0
# while cnt !=5:
#     for d in range(111, n, 100):
#         if n % d ==0:
#             cnt +=1
#             print(n, d)
#             break
#     n +=1



# for n in range(600):
#     deli = []
#     for d in range(17, n, 10):
#         if n %d ==0:
#             deli.append(d)
#     if deli:
#         print(len(deli))

# 25

# def pros(n):
#     for i in range(2, n):
#         if n % i ==0:
#             return 0
#     return n >1
#
#
# for n in range(1000001, 1000001+10000):
#     deli = []
#     for d in range(2, n):
#         if n % d ==0:
#             deli.append(d)
#     if deli and pros(max(deli)):
#         print(n, max(deli))


# for n in range(800001, 800001+10000):
#     F = 0
#     deli = []
#     for d in range(2, n):
#         if n % d ==0:
#             deli.append(d)
#     if deli:
#         deli.sort()
#         F = min(deli)* deli[-2]
#     if F !=0 and F % (deli[0] + deli[1]) == 0:
#         print(n, F)

# # 25d
# for n in range(200123, 200151):
#     deli = []
#     for d in range(1, 200151):
#         if n % d == 0:
#             deli.append(d)
#     if len(deli) == 4:
#         print(deli)


# for n in range(14620, 15001):
#     deli = []
#     for d in range(2, n):
#         if n % d ==0:
#             deli.append(d)
#     if len(deli)==3:
#         print(n, min(deli))



# for n in range(700001, 700001+10000):
#     F =0
#     deli = []
#     for d in range(2, n):
#         if n %d==0:
#             deli.append(d)
#     if deli:
#         F = max(deli) - min(deli)
#     if F !=0 and F % 9 ==0:
#         print(n, F)

# for n in range(600001, 600001+10000):
#     deli = []
#     for d in range(17, n, 10):
#         if n % d ==0:
#             deli.append(d)
#     if deli:
#         print(n, min(deli))

#
# def pros(n):
#     for i in range(2, n):
#         if n % i ==0:
#             return 0
#     return n >1
#
# for n in range(610001, 610001+10000):
#     deli = []
#     for d in range(2, n):
#         if n % d ==0:
#             deli.append(d)
#     if deli and pros(max(deli)):
#         print(n, max(deli))



# from turtle import *
# tracer(0)
# speed(0)
# k = 100
# pendown()
# begin_fill()
# for i in range(5):
#     forward(82*k)
#     left(72)
# end_fill()
# penup()
# canvas= getcanvas()
# cnt =0
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         if canvas.find_overlapping(x*k, y*k, x*k, y*k)== (5,):
#             cnt +=1
# print(cnt)
# done()


