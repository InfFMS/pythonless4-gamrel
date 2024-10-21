# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
def MinMax(X, Y):
    A=1
    if (X>Y): n=X
    else: n=Y
    while (n>0):
        if (X/n==X//n)and(Y//n==Y/n):
            a=n
            if (A<a): A=a
        n-=1
    print(A)
X=int(input())
Y=int(input())
print(MinMax(X, Y))

