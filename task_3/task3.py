# Напишите программу, которая считывает данные из
# CSV-файла sales.csv, где содержатся данные о продажах
# (например, дата, товар, количество, цена).
# Программа должна вывести:
# - Общую сумму продаж.
# - Товар с наибольшим числом продаж.
import csv
d = {}
total = 0
with open('products.csv', 'r', encoding='utf-8') as file:
    f = csv.DictReader(file)
    for i in f:
        quantity = int(i['quantity'])
        price = float(i['price'])
        count = quantity * price
        total += count
        product = i['product']
        if product in d:
            d[product] += count
        else:
            d[product] = count
sorts = sorted(d.items())
print(*sorts[0])
print(total)