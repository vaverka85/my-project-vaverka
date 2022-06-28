#Task1:Напишите функцию, которая будет принимать номер кредитной карты и
# # показывать только последние 4 цифры. Остальные цифры должны заменяться
# # звездочками
def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]
print(card_hide('1234567891021236'))
print(card_hide('7894561237894651'))

#Task2:Напишите функцию, которая проверяет: является ли слово палиндромом
word = (input('Введите слово: '))
def polindrom(word):
    a = ''.join(word.split())
    print(a)
    b = word[::-1]
    if word == b:
        print('Это полиндром!')
    else:
        print('Обычное слово.')
polindrom(word)

