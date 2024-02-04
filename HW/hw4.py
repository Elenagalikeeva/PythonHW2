sum = 0
a = [float(input("Введите число: ")) for i in range(int(input(" Введите кол-во чисел последовательности: ")))]
print("Кол-во чисел: ", len(a))
for i in range(len(a)):
    sum += a[i]
print("Среднее арифметическое: ", sum/len(a))
print("Мин число: ", min(a))
print("Макс число: ", max(a))




