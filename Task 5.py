# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math

first_list = [float(input('Введите координату X первой точки ')), float(input('Введите координату Y первой точки '))]
second_list = [float(input('Введите координату X второй точки ')), float(input('Введите координату Y второй точки '))]
result = math.sqrt(pow(first_list[0] - second_list[0], 2) + (pow(first_list[1] - second_list[1], 2)))
print(f'Расстояние между двумя точками = {round(result, 2)}')