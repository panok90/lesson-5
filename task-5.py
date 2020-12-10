"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from functools import reduce

str_numbers = input("Введите числа через пробел: ")

with open("task-5.txt", "w") as object_file:
    object_file.write(str_numbers)
list_numbers = str_numbers.split()
print(reduce(lambda a, b: int(a) + int(b), list_numbers))
