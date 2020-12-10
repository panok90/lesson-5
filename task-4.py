"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

list_number_ru = ['один', 'два', 'три', 'четыре']
item = 0
new_list = list()
with open("task-4_en.txt", encoding="utf-8") as object_file:
    str_list = object_file.readlines()
for line in str_list:
    list_line = line.split(' — ')
    list_line[0] = list_number_ru[item]
    new_list.append(' — '.join(list_line))
    item += 1
with open("task-4_ru.txt", "w", encoding="utf-8") as object_file:
    object_file.writelines(new_list)
