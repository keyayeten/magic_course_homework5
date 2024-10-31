#   В файле employees.csv содержится список сотрудников
# с полями: имя, возраст, должность, зарплата.
# Напишите программу, которая считывает данные
# и выводит только тех сотрудников,
# у которых зарплата больше 50,000.
import csv

with open("employees.csv", "r", encoding="utf-8") as file:
    employees = list(csv.DictReader(file))

list_who_earn_more_50k = []
for employee in employees:
    if "salary" in employee:
        salary = int(employee.get("salary"))
        if salary > 50000:
            list_who_earn_more_50k.append(employee)
print(list_who_earn_more_50k)
