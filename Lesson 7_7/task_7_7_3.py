'''
Подвиг 4. Вводится натуральное число N. Необходимо с помощью рекурсивной функции fib_rec(N, f=[])
(здесь N - общее количество чисел Фибоначчи; f - начальный список этих чисел) сформировать последовательность чисел Фибоначчи по правилу:
первые два числа равны 1 и 1, а каждое следующе значение равно сумме двух предыдущих.
Пример такой последовательности для первых 7 чисел: 1, 1, 2, 3, 5, 8, 13, ...

Функция должна возвращать список сформированной последовательности длиной N.

Вызывать функцию не нужно, только объявить.

Sample Input:
7
Sample Output:
1 1 2 3 5 8 13
'''

# ввод числа N
N = int(input())

# здесь задается функция fib_rec (переменную N не менять!)
def fib_rec(N, f=[]):
    if N > len(f):
        f.append(1 if len(f) < 2 else f[-1] + f[-2])
        fib_rec(N, f)
        return f