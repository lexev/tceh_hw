"""Реализовать две функции: write_to_file(data) и read_file_data().
Которые соотвественно: пишут данные в файл и читают данные из файла."""

import os

def write_to_file(data, path, file):
    with open(os.path.join(path, file), 'w') as w_file:
        w_file.write(data)


def read_file_data(path, file):
    with open(os.path.join(path, file), 'r') as r_file:
        print(r_file.read())


if __name__ == "__main__":
      write_to_file('my data', '', '1.txt') #путь для простоты в этой же директории
      read_file_data('', '1.txt') #путь для простоты в этой же директории
