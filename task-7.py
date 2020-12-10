"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json

dict_firm = dict()
sum_el = 0
count = 0
with open("task-7.txt") as object_file:
    for n, line in enumerate(object_file, 1):
        line = line.rstrip('\n')
        list_el = line.split()
        dict_key_firm = list_el[0]
        profit = int(list_el[2]) - int(list_el[3])
        if profit > 0:
            sum_el += profit
            count += 1
        dict_firm[dict_key_firm] = profit
dict_average_profit = {"average_profit": sum_el/count}
list_result = [dict_firm, dict_average_profit]
print(list_result)
with open("task-7.json", "w") as object_json:
    json.dump(list_result, object_json)
