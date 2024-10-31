# В файле users.json хранится список пользователей с полями:
# имя, возраст, город и профессия. Напишите программу,
# которая считывает файл и выводит только тех пользователей,
# которые старше 30 лет и работают в указанной профессии.
import json

with open("task2.json", "r", encoding="utf-8") as file:
    data = json.load(file)

list_who_over_30 = []

for person in data:
    if "age" in person:
        age = person.get("age")
        if age >= 30:
            list_who_over_30.append(person)

print(list_who_over_30)
