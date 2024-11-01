# В файле users.json хранится список пользователей с полями:
# имя, возраст, город и профессия. Напишите программу,
# которая считывает файл и выводит только тех пользователей,
# которые старше 30 лет и работают в указанной профессии.
import json

lst = []
with open('task2.json', 'r', encoding='utf-8') as file:
    f = json.load(file)
    print(f)
    for k in f:
        if k['age'] > 30 and 'profession' == 'программист':
            lst.append(k)
print(*lst)




