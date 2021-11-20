from Functions import *

print('Введите матрицу A')
A = matrix_init()
while len(A) < 0:
    print('Ошибка! - пустая матрица')
    print('Введите матрицу A')
    A = matrix_init()
print('Введите матрицу B той же размерности')
B = matrix_init(len(A), len(A[0]))

C = []
for a, b in zip(A, B):
    new = []
    for j, m in zip(a, b):
        new.append(j * m)
    C.append(new)

print('Матрица C')
print_matrix(C)
print()

V = [0] * len(C[0])
for i in C:
    for j in range(len(i)):
        V[j] += i[j]
print('Массив V:', V)
