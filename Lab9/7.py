from Functions import *

arr = matrix_init(type=str)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        for c in arr[i][j]:
            if c in 'aeiouyAEIOUY':
                arr[i][j] = arr[i][j].replace(c, '.')
print_matrix(arr, type=str)