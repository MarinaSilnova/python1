#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
xa = int(input('введите координату х точки А: '))
ya = int(input('введите координату y точки А: '))
xb = int(input('введите координату х точки B: '))
yb = int(input('введите координату y точки B: '))
lenghtAB = ((xb - xa)**2 + (yb - ya)**2)**0.5
print(round(lenghtAB, 2))
