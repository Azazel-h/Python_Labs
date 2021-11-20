from Functions import *

print('Пожалуйста введите данные для создания квадратной матрицы')
D = list(map(int, input('Введите элементы массива D через пробел: ').split()))
F = list(map(int, input('Введите элементы массива F через пробел: ').split()))
while len(D) != len(F):
    print('Пожалуйста введите данные именно для квадратной матрицы')
    D = list(map(int, input('Введите элементы массива D через пробел: ').split()))
    F = list(map(int, input('Введите элементы массива F через пробел: ').split()))

arr = create_matrix(D, F)

print_matrix(arr)
for i in range(len(arr)):
    for j in range(i):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print('Транспонированная матрица: ')
print_matrix(arr)