'''
Подвиг 6. Имеется список базовых нот:

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, в одну строчку через пробел.
Необходимо отобразить указанные ноты в виде строки через пробел, но перед нотами до и фа дополнительно ставить символ диеза '#'.
Реализовать эту программу с использованием тернарного условного оператора (он может использоваться несколько раз).

Sample Input:
1 6 7
Sample Output:
#до ля си
'''

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b , c = map(int, input().split())
note1 = '#' + m[a - 1] if a == 1 or a == 4 else m[a - 1]
note2 = '#' + m[b - 1] if b == 1 or b == 4 else m[b - 1]
note3 = '#' + m[c - 1] if c == 1 or c == 4 else m[c - 1]
print(note1, note2, note3)