# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input('Введите цифру '))
if (0 < number < 6):
    print('Данный день не является выходным')
elif (number == 6 or number == 7):
    print('Данный день являтся выходным')
else:
    print('Такого дня в неделе не существует')