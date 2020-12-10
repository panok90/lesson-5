"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

dict_item = dict()
with open("task-6.txt", encoding="utf-8") as object_file:
    list_schedule = object_file.readlines()
for el in list_schedule:
    list_item = el.split(":")
    dict_key = list_item[0]
    list_value = list_item[1].split()
    sum_value = 0
    for item in list_value:
        if item == "—":
            continue
        item_value = item.split("(")
        sum_value += int(item_value[0])
    dict_item[dict_key] = sum_value
print(dict_item)