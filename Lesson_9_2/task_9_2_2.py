'''
Подвиг 2. Мы с вами в заданиях несколько раз генерировали последовательность чисел Фибоначчи, которая строится по правилу:
каждое последующее число равно сумме двух предыдущих.
Для разнообразия давайте будем генерировать каждое последующее как сумму трех предыдущих чисел.
При этом первые три числа равны 1 и имеем такую последовательность:

1, 1, 1, 3, 5, 9, 17, 31, 57, ...

Не знаю, есть ли у нее название, поэтому, в рамках уроков, я скромно назову ее последовательностью Балакирева.

Итак, на вход программы поступает натуральное число N (N > 5) и необходимо определить функцию-генератор,
которая бы возвращала N первых чисел последовательности Балакирева (включая первые три единицы).

Реализуйте эту функцию без использования коллекций (списков, кортежей, словарей и т.п.).
Вызовите ее N раз для получения N чисел и выведите полученные числа на экран в одну строчку через пробел.

Sample Input:
7
Sample Output:
1 1 1 3 5 9 17
'''

N = int(input())

def get_fib(N):
    x1, x2, x3 = 1, 1, 1
    for i in range(N):
        if i >= 3:
            x1, x2, x3 = x2, x3, x1 + x2 + x3
        yield x3

gen = get_fib(N)
for i in range(N):
    print(next(gen), end=' ')