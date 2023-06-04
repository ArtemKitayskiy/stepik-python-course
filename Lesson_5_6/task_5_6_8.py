'''
Подвиг 8. В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64.
Вводится натуральное число n. Как наименьшим количеством таких денежных купюр можно выплатить сумму n?
Вывести на экран список купюр для формирования суммы n (в одну строчку через пробел, начиная с наибольшей и заканчивая наименьшей).
Предполагается, что имеется достаточно большое количество купюр всех достоинств.

Sample Input:
221
Sample Output:
64 64 64 16 8 4 1
'''

money = [1, 2, 4, 8, 16, 32, 64]
n = int(input())
pay = []

for i in range(1, len(money)+1):
    if n // money[-i] >= 1:
        pay += (n // money[-i]) * [money[-i]]
        n -= (n // money[-i]) * money[-i]
print(*pay)