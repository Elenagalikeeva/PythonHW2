name = input('Введите ФИО:')
first = name[:name.find(" ")]
second = name[name.find(" "):name.find(" ")+2]
third = name[name.rfind(" "): name.rfind(" ")+2]
print(first+second+third)
