'''
Подвиг 1. Имеется следующее меню:

m = \'''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход\'''
В программе вводится целое число от 1 до 6.
Нужно вывести пункт меню, связанный с этим числом. Реализовать программу с использованием операторов if-elif

Sample Input:
2
Sample Output:
2. Строки и списки
'''

m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

lst = m.split('\n')
i = input()

if lst[0][0] == i:
    print("1. Введение в Python")
elif lst[1][0] == i:
    print("2. Строки и списки")
elif lst[2][0] == i:
    print("3. Условные операторы")
elif lst[3][0] == i:
    print("4. Циклы")
elif lst[4][0] == i:
    print("5. Словари, кортежи и множества")
elif lst[5][0] == i:
    print("6. Выход")