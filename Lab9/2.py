from Functions import *

D = list(map(int, input('Введите элементы массива D через пробел: ').split()))
F = list(map(int, input('Введите элементы массива F через пробел: ').split()))
arr = create_matrix(D, F)
print_matrix(arr)

main = []
sub = []
for i in range(len(arr)):
    for j in range(len(arr[i]) - 1, i, -1):
        main.append(arr[i][j])
print(f'MAX: {max(main):.5f}')
for i in range(len(arr)):
    for j in range(len(arr[i]) - i, len(arr[i])):
        sub.append(arr[i][j])
print(f'MIN: {min(sub):.5f}')