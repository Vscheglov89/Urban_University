import io
from pprint import pprint

file_name = "test.txt"

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    num_str = 0
    for string in strings:
        num_str += 1
        byte_1 = file.tell()
        file.write(string + '\n')
        strings_positions[(num_str, byte_1)] = string
    return strings_positions
    file.close()


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
