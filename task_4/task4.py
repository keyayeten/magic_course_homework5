#   В файле employees.csv содержится список сотрудников
# с полями: имя, возраст, должность, зарплата.
# Напишите программу, которая считывает данные
# и выводит только тех сотрудников,
# у которых зарплата больше 50,000.
import csv

with open('employees.csv', 'r', encoding='utf-8') as file:
    f = csv.DictReader(file)
    for i in f:
        if int(i['salary']) > 50000:
            print(i)
