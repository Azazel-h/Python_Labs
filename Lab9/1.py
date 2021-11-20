from Functions import *

D = list(map(int, input('Введите элементы массива D через пробел: ').split()))
F = list(map(int, input('Введите элементы массива F через пробел: ').split()))
arr = create_matrix(D, F)

AV = []
L = []
for i in arr:
    positive = [k for k in i if k > 0]
    if len(positive) > 0:
        avg = get_average(positive)
        AV.append(avg)
        counter = 0
        for j in i:
            if j < avg:
                counter += 1
        L.append(counter)
    else:
        AV.append('')
        L.append('')

for i, avg, l in zip(arr, AV, L):
    for num in i:
        print(f'{num:>10.5f}', end=' ')
    print(f'{avg:>15.5f}{l:>4}' if avg else f'{avg:>10}{l:>4}')
