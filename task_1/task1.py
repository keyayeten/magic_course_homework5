# Напишите программу, которая сравнивает два JSON-файла
# (task1_1.json и task1_2.json) и выводит различия между ними.
# Программа должна определить, какие ключи или значения отличаются.
# Сравнивать только ключи и значения первого уровня.
import json

d1 = {}
d2 = {}
with open('task1_1.json', 'r', encoding='utf-8') as file:
    r1 = json.load(file)
    for k, v in r1.items():
        d2[k] = v
print(d2)

with open('task1_2.json', 'r', encoding='utf-8') as file:
    r2 = json.load(file)
    for k, v in r2.items():
        d1[k] = v
print(d1)

d3 = {}
for i in d1:
    if i not in d2: #если ключа нет во втором словаре
        d3[i] = d1[i]

for j in d2:
    if j not in d1:
        d3[j] = d2[j]
    elif d1[j] != d2[j]:
        d3[j] = d1[j], d2[j]
print(d3)