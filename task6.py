# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3
def MinMax(X, Y):
    A=1
    C=X
    c=Y
    while ((X%A==0)and(Y%A==0)):
        A = 1
        if (X > Y):
            n = X
        else:
            n = Y
        while (n > 0):
            if (X / n == X // n) and (Y // n == Y / n):
                a = n
                if (A < a): A = a
            n -= 1
        if (X%A==0)and(Y%A==0):
            X=X/A
            Y=Y/A
        if ((X%A<1)and(Y%A<1)): return (print(C, c))
    print (X,Y)
X=int(input())
Y=int(input())
MinMax(X, Y)
