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