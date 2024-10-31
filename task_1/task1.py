# Напишите программу, которая сравнивает два JSON-файла
# (file1.json и file2.json) и выводит различия между ними.
# Программа должна определить, какие ключи или значения отличаются.
# Сравнивать только ключи и значения первого уровня.
import json

with open("task1_1.json", "r", encoding="utf-8") as file:
    json1 = dict(json.load(file))

with open("task1_2.json", "r", encoding="utf-8") as file:
    json2 = dict(json.load(file))

keys_in_json1 = set(json1.keys())
keys_in_json2 = set(json2.keys())

keys_only_in_json1 = keys_in_json1.difference(keys_in_json2)
keys_only_in_json2 = keys_in_json2.difference(keys_in_json1)

new_dict = {
    "keys_only_json1": keys_only_in_json1,
    "keys_only_json2": keys_only_in_json2
}

for key, value in json1.items():
    for key2, value2 in json2.items():
        if key == key2 and value != value2:
            new_dict[key] = [value, value2]

print(new_dict)
