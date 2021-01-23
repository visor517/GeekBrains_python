# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
print('Задание 6*')

data = []
for id in range(1, 4):
    name = input(f'Введите название товара {id}: ')
    price = int(input(f'Введите стоимоть товара {id}: '))
    quantity = int(input(f'Введите количество товара {id}: '))
    unit = input(f'Введите единицы измерения {id}: ')
    data.append((id, {"название": name, "цена": price, "количество": quantity, "ед": unit}))

result = {"название": [], "цена": [], "количество": [], "ед": []}
for good in data:
    for key, value in good[1].items():
        if result[key].count(value) == 0:
            result[key].append(value)

print(result)
