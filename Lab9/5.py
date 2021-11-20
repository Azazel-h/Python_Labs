from Functions import *

print('Введите матрицу D')
D = matrix_init()
print('Введите матрицу Z')
Z = matrix_init(len(D))
G = []

print('Матрица D до преобразований:')
print_matrix(D)
print()
for d, z in zip(D, Z):
    z_sum = sum(z)
    counter = 0
    for j in d:
        if j > z_sum:
            counter += 1
    G.append(counter)
max_G = max(G)
D = [[j * max_G for j in i] for i in D]

print('Матрица D после преобразования:')
print_matrix(D)
