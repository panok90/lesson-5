"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

with open('task-2.txt', encoding='utf-8') as object_file:
    str_list = object_file.readlines()
count_str = len(str_list)
print(f'Количество строк: {count_str}')
item = 1
for line in str_list:
    list_word = line.split()
    print(f'В {item} строке: {len(list_word)} слов(а)')
    item += 1
