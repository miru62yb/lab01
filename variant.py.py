#todo название заказа и имя заказчика.
order_name = input("Введите название заказа: ")
customer_name = input("Введите имя заказчика: ")

#todo Название, количество и цена единицы в рублях.
name1 = input("Введите название первой позиции: ")
count1 = int(input("Введите количество первой позиции: "))
price1 = float(input("Введите цену за единицу первой позиции: "))

name2 = input("Введите название второй позиции: ")
count2 = int(input("Введите количество второй позиции: "))
price2 = float(input("Введите цену за единицу второй позиции: "))

#todo Стоимость доставки и лишённую (внесённую) сумму.
delivery_cost = float(input("Введите стоимость доставки: "))
paid_amount = float(input("Введите внесённую сумму: "))

#todo Рассчет стоимости каждой позиции, стоимость товаров без доставки, общую сумму с доставкой, общее количество единиц и сдачу.
cost1 = count1 * price1
cost2 = count2 * price2
goods_cost = cost1 + cost2
total_cost = goods_cost + delivery_cost
total_count = count1 + count2
change = paid_amount - total_cost

#todo итоговый вывод информации о заказе.
print(f"Заказ: {order_name}")
print(f"Заказчик: {customer_name}")
print(f"{name1} | {count1} | {price1:.2f} | {cost1:.2f}")
print(f"{name2} | {count2} | {price2:.2f} | {cost2:.2f}")
print(f"Стоимость товаров без доставки: {goods_cost:.2f}")
print(f"Общая сумма с доставкой: {total_cost:.2f}")
print(f"Общее количество единиц: {total_count}")
print(f"Сдача: {change:.2f}")