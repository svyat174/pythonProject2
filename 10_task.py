# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')


table_code = goods['Стол']
table_items1 = store[table_code][0]
table_items2 = store[table_code][1]
table_quantity = table_items1['quantity'] + table_items2['quantity']
table_price = table_items1['price'] + table_items2['price']
table_coast = table_price * table_quantity

print('Стол -', table_quantity, 'шт, стоимость', table_coast, 'руб')

sofa_code = goods['Диван']
sofa_items1 = store[sofa_code][0]
sofa_items2 = store[sofa_code][1]
sofa_quantity = sofa_items1['quantity'] + sofa_items2['quantity']
sofa_price = sofa_items1['price'] + sofa_items2['price']
sofa_coast = sofa_price * sofa_quantity

print('Стол -', sofa_quantity, 'шт, стоимость', sofa_coast, 'руб')

chair_code = goods['Стул']
chair_items1 = store[chair_code][0]
chair_items2 = store[chair_code][1]
chair_items3 = store[chair_code][2]
chair_quantity = chair_items1['quantity'] + chair_items2['quantity'] + chair_items3['quantity']
chair_price = chair_items1['price'] + chair_items2['price'] + chair_items2['price']
chair_coast = chair_price * chair_quantity

print('Стол -', chair_quantity, 'шт, стоимость', chair_coast, 'руб')