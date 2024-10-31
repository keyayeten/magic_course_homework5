# Напишите программу, которая считывает данные из
# CSV-файла sales.csv, где содержатся данные о продажах
# (например, дата, товар, количество, цена).
# Программа должна вывести:
# - Общую сумму продаж.
# - Товар с наибольшим числом продаж.
import csv

with open("products.csv", "r", encoding="utf-8") as file:
    products = list(csv.DictReader(file))

total = 0
for product in products:
    if "quantity" and "price" in product:
        price = float(product.get("price"))
        quantity = float(product.get("quantity"))
        sum_all_products = quantity * price
        total += sum_all_products

print(f"Общая сумма продаж: {total}")

max_sell_product = []
quantity = 0
for product in products:
    if "quantity" in product:
        quantity_of_one_product = float(product.get("quantity"))
        if quantity_of_one_product > quantity:
            max_sell_product.clear()
            max_sell_product.append(product)
            quantity = quantity_of_one_product

print(f"Товар с наибольшим числом продаж: {max_sell_product}")
