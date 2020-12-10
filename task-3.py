"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open('task-3.txt', encoding='utf-8') as object_file:
    str_list = object_file.readlines()
count_list = len(str_list)
list_worker = list()
average_sum = 0
for el in str_list:
    list_el = el.split()
    average_sum += float(list_el[1])
    if float(list_el[1]) < 20000:
        list_worker.append(list_el[0])

print(list_worker)
print(round(average_sum/count_list, 2))
