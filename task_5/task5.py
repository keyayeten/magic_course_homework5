# Система учета заказов

# У вас есть JSON-файл orders.json,
# содержащий данные о заказах интернет-магазина.
# Каждый заказ включает информацию о клиенте,
# заказанных товарах, количестве и цене.
# Напишите программу, которая:
# Выводит общую сумму каждого заказа.
# Находит клиента с наибольшей суммой заказа и выводит его имя и сумму.
import json


with open("orders.json", "r", encoding="utf-8") as file:
    orders = dict(json.load(file))

orders = orders.get("orders")

start_order_id = orders[0]
start_order_id = dict(start_order_id).get("order_id")

sum_one_order = 0
sum_one_order_for_cards_top_customer = 0
dict_sum_orders = []
cards_top_customer = []
top_total_order = 0

for order in orders:

    order_id = dict(order).get("order_id")
    items1 = dict(order).get("items")
    customer = dict(order).get("customer")
    name = dict(customer).get("name")

    if order_id != start_order_id:
        start_order_id = order_id
        sum_one_order = 0
    for item in items1:
        if "quantity" and "price" in item:
            quantity = item.get("quantity")
            price = item.get("price")
            sum_one_item = quantity * price
            sum_one_order += sum_one_item
    else:
        dict_sum_orders.append({"order_id": order_id, "sum_one_order": sum_one_order})

        if sum_one_order > sum_one_order_for_cards_top_customer:
            cards_top_customer.clear()
            cards_top_customer.append({"name": name, "max_sum_order": sum_one_order})
            sum_one_order_for_cards_top_customer = sum_one_order
        elif sum_one_order == sum_one_order_for_cards_top_customer:
            cards_top_customer.append({"name": name, "max_sum_order": sum_one_order})

print(dict_sum_orders)
print(cards_top_customer)

