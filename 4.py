#Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
number = int(input('введите число N: '))
start = 1
while start <= number:
    if start % 2 == 0:
        print(start, end= ' ')
    start+=1
