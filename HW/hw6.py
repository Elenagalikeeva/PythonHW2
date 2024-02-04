n = [int(input("введите элементы списка: ")) for i in range(int(input("n= ")))]
k = int(input("введите индекс: "))
print("k=", k)
c = int(input("введите значение: "))
print("c=", c)
n.insert(k, c)
print(n)