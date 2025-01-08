'''Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой
функции будет простым числом и "Составное" в противном случае.

Пример:
result = sum_three(2, 3, 6)
print(result)'''


def is_prime(func):  # Декораторр.
    def wrapper(a, b, c):
        sum_three_result = func(a, b, c)

        if sum_three_result < 2:
            return f'Ни простое, ни составное\n{sum_three_result}'

        for i in range(2, sum_three_result):
            if sum_three_result % i == 0:
                return f'Составное\n{sum_three_result}'

        return f'Простое\n{sum_three_result}'

    return wrapper


@is_prime
def sum_three(a, b, c): # Декорируемая
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
