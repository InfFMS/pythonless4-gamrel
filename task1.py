# Напишите процедуру, которая принимает параметр – натуральное число N –
# и выводит на экран треугольник из * с катетами равными N.
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
def add(N):
    c=('*')
    n=0
    a=1
    while (n<N):
        print(a*c)
        a+=1
        N-=1
N = int(input())
add(N)
