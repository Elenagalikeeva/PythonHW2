students = {}
a = 0
kolstud = int(input("Кол-во студентов:"))
for i in range(1, kolstud + 1):
    stud = input(str(i) + "-й студент: ")
    score = int(input("Балл:"))
    students[stud] = score
    a += score
sred= a/kolstud
print(sred)
for i in students:
    if students[i]> sred:
        print("Студенты с баллом выше среднего:", i)



