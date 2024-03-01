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


for i in range(151, 1000):
    a = "7" * i
    while "777" in a:
        a = a.replace("777", "111", 1)
        a = a.replace("1111", "7", 1)
    if a == "711":
        print(i)
        break
