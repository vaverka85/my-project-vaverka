#Task 1:
a = input('Введите первое числo: ')
b = input('Введите второе числo: ')
try:
    c = int(a) / int(b)
except ZeroDivisionError as error:
    print()
    print('Произошла ошибка деление на ноль')
    print('Цепочка наследования:')
    for s in error.__class__.__mro__:
        print(s.__name__)
except ValueError as error:
    print(error)
    print('Ошибка ввода, неверный формат данных. Попробуйте еще раз.')
    print('Цепочка наследования:')
    for s in error.__class__.__mro__:
        print(s.__name__)
else:
    print('Все хорошо! Результат', c)

#Task 2:
#Проверить, есть ли в последовательности чисел списка дубликаты. Без использования множества.
from random import random
n = 10
arr = [0] * n
for i in range(n):
    arr[i] = int(random()*50)
print(arr)
for i in range(n-1):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print('Есть одинаковые')
            quit()
print('Все элементы уникальные')





