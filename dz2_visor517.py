# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа
# данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не
# запрашивать у пользователя, а указать явно, в программе.
myList = [17, 85.2, 'строка', True, [1, 2, 3], None, 'the end']

for item in myList:
    print(item, '-', type(item))

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
yourList = input('2: Введите список элементов разделенных пробелами: ')

yourList = yourList.split(' ')
i = 0
while i < len(yourList):
    if i + 1 < len(yourList):
        yourList[i], yourList[i+1] = yourList[i+1], yourList[i]
    i = i + 2

print(yourList)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
month = int(input('3: Введите месяц в виде целого числа от 1 до 12: '))

if month in range(3, 6):
    result = 'Весна'
elif month in range(6, 9):
    result = 'Лето'
elif month in range(9, 12):
    result = 'Осень'
elif month in range(1, 3) or 12:
    result = 'Зима'
else:
    result = 'Введено неподходящее значение!'

print(result)

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
string = input('4: Введите строку из нескольких слов, разделённых пробелами: ')

string_list = string.split(' ')

for index, item in enumerate(string_list):
    word = item[:10] if len(item) > 10 else item
    print(f'{index+1} : {word}')

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У
# пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.

rate = [7, 5, 3, 3, 2]
print(f'5: {rate}')
mark = int(input('Введите новый элемент рейтинга: '))

if rate[-1] < mark:
    for index, item in enumerate(rate):
        if mark > item:     # индекс первого числа меньше введенного
            break;

    result = rate[:index] + [mark] + rate[index:]
else:
    result = rate + [mark]

print(result)

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
