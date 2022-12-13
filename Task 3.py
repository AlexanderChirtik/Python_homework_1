# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .

x_coordinate = float(input('Введите координату X '))
y_coordinate = float(input('Введите координату Y '))
if (x_coordinate == 0 or y_coordinate == 0):
    print('Координаты X и Y не могут быть равны 0')
else:
     if (x_coordinate > 0 and y_coordinate > 0):
        print('Координаты X и Y находятся в первой четверти')
     elif (x_coordinate < 0 and y_coordinate > 0):
        print('Координаты X и Y находятся во второй четверти')
     elif (x_coordinate < 0 and y_coordinate < 0):
        print('Координаты X и Y находятся в третьей четверти')
     elif (x_coordinate > 0 and y_coordinate < 0):
        print('Координаты X и Y находятся в четвертой четверти')
