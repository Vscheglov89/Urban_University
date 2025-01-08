'''Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.'''


def all_variants(text):
    length = len(text)
    for size in range(1, length + 1):
        for start_index in range(length - size + 1):
            yield text[start_index:start_index + size]


all = all_variants('abc')
for i in all:
    print(i)
