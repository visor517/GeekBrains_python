# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и
# арифметические операции.

n = int(input('Введите целое положительное число: '))

maximum = 0

while n > 0:
    if n % 10 > maximum:
        maximum = n % 10
    n = n // 10

print(f'Наибольшее число: {maximum}')