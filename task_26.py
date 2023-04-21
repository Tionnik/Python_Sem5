# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

a=int(input("Введите число А: "))
b=int(input("Введите число B: "))
def degree (a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    elif b > 1:
        n=degree(a,1)*degree(a,(b-1))
        return n
    
print(degree(a,b))
