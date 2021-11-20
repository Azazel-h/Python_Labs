from Functions import *

print('Пожалуйста введите данные для создания квадратной матрицы')
D = list(map(int, input('Введите элементы массива D через пробел: ').split()))
F = list(map(int, input('Введите элементы массива F через пробел: ').split()))
while len(D) != len(F):
    print('Пожалуйста введите данные именно для квадратной матрицы')
    D = list(map(int, input('Введите элементы массива D через пробел: ').split()))
    F = list(map(int, input('Введите элементы массива F через пробел: ').split()))

arr = create_matrix(D, F)

print('Ваша изначальная матрица: ')
print_matrix(arr)
print()

for i in range(len(arr)):
    for j in range(i):
        arr[j][i], arr[i][j] =  arr[i][j], arr[j][i]

print('Промежуточная матрица: ')
print_matrix(arr)
print()

arr = [i[::-1] for i in arr]

print('Матрица повернутая на 90 градусов по часовой стрелке: ')
print_matrix(arr)
print()

for i in range(len(arr)):
    for j in range(i):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print('Промежуточная матрица: ')
print_matrix(arr)
print()

print('Матрица повернутая на 90 градусов против часовой стрелки: ')
arr = arr[::-1]

print_matrix(arr)