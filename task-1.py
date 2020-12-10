"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

str_list = list()
with open(f'task-1.txt', 'w') as object_file_text:
    while True:
        str_input = input("Введите строку: ")
        if not str_input:
            break
        str_list.append(f'{str_input}\n')
    object_file_text.writelines(str_list)
