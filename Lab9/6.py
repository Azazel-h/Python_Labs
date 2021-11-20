from Functions import *

print('Введите матрицу D')
D = matrix_init()
I = list(map(int, input('Введите массив I через пробел: ').split()))
R = []

if len(D) > 0:
    for i in I:
        R.append(max(D[i]))
else:
    print('Ошибка! - Пустая матрица')
    print()

print('Матрица D:')
print_matrix(D)
print('Массив I:', I)
if len(R) > 0:
    print('Массив R:', R)
    avg = sum(R) / len(R)
    print('Среднее арифметическое:',avg)
