import itertools
import random


def generate_password(n): # Генерируем уникальные пары чисел
    numbers = list(range(1, n + 1))
    pairs = list(itertools.combinations(numbers, 2))
    password = ""  # Инициализируем пароль

    for pair in pairs: # Проверяем кратность для каждой пары
        pair_sum = sum(pair)
        if n % pair_sum == 0:
            password += str(pair[0]) + str(pair[1])  # Добавляем пару в пароль
    return password


n = random.randint(3, 20) # Генерируем число от 3 до 20
result = generate_password(n)
print(f'Заданное число: {n}')
print(f'Нужный пароль: {result}')
