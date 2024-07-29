
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and third:
    print('Все числа равны')
elif first == second or first == third or second == third:
    print('Два числа равны между собой')
else:
    print('Равных чисел не найдено')