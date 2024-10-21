# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять
def chet(n):
     k1 = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
          6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
     k2 = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
          50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
          80: 'восемьдесят', 90: 'девяносто'}
     k3 = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
          14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
          17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
     n1 = n % 10
     n2 = n - n1
     if (n < 10): print(k1.get(n))
     elif (n%10==0): print(k2.get(n))
     elif (n > 20):print(k2.get(n2) + ' ' + k1.get(n1))
     else: print(k3.get(n))
n = int(input())
print(chet(n))