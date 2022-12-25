#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти
number = int(input('введите номер четверти: '))
if number == 1:
    print(f'{number} -> x > 0, y > o')
elif number == 2:
    print(f'{number} -> x < 0, y > o')
elif number == 3:
    print(f'{number} -> x < 0, y < o')
elif number == 4:
    print(f'{number} -> x > 0, y < o')
else:
    print('Некорректно введен номер четверти')