# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
def mnog(x):
    n=2
    l=str('')
    a=0
    c='*'
    while (x>n):
        while (x%n==0):
            x=x//n
            a+=1
        if (a>0): l+=str(a)+(c)+str(n)
        n+=1
        a=0
    l+=c+str(x)
    return print(l)
x=int(input())
print (mnog(x))

