'''Создайте функцию read_info(name), где name - название файла. Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.
Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
Создайте список названий файлов в соответствии с названиями файлов архива.
Вызовите функцию read_info для каждого файла по очереди (линейно) и измерьте время выполнения и выведите его в консоль.
Вызовите функцию read_info для каждого файла, используя многопроцессный подход: контекстный менеджер with и объект Pool.
Для вызова функции используйте метод map, передав в него функцию read_info и список названий файлов.
Измерьте время выполнения и выведите его в консоль.'''

from typing import List
import time
from multiprocessing import Pool
from multiprocessing import freeze_support


def read_info(name: str) -> List[str]:
    all_data = []
    with open(name, 'r') as file:  # Открывать файл name для чтения
         while True:
            line = file.readline()  # Считывать информацию построчно
            if not line:
                break
            all_data.append(line.strip())  # добавлять каждую строку в список
    return all_data

def main():
    file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt'] #список названий файлов

    start_time = time.time() #read_info для каждого файла по очереди (линейно)
    for file in file_names:
        read_info(file)
    end_time = time.time()

    elapsed_time_linear = end_time - start_time
    print(f"Время выполнения линейного вызова: {elapsed_time_linear} секунд")


    start_time = time.time() #read_info для каждого файла, используя многопроцессный подход
    with Pool() as pool:
        results = pool.map(read_info, file_names)
    end_time = time.time()

    elapsed_time_parallel = end_time - start_time
    print(f"Время выполнения многопроцессного вызова: {elapsed_time_parallel} секунд")


if __name__ == '__main__':
    freeze_support()
    main()

# линейный вызов оказался быстрее.

