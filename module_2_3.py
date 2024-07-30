my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
print('Список', my_list)
while a < len(my_list):
    number = my_list[a]
    a = a + 1
    if number == 0:
        continue
    elif number < 0:
        print('отрицательное число:', number)
        break
    elif a == len(my_list):
        print(number)
        print('конец списка')
    else:
        print(number)
