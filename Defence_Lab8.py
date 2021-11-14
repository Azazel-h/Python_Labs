matrix = []
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
for i in range(n):
    new = []
    for j in range(m):
        element = input(f'Введите {j} элемент {i} строки: ')
        new.append(element)
    matrix.append(new)

columns_digit_count = dict.fromkeys([i for i in range(m)], 0)
for i in range(n):
    for j in range(m):
        for c in matrix[i][j]:
            if c.isdigit():
                columns_digit_count[j] += 1

arr = [k for k, v in columns_digit_count.items() if v % 2 != 0]
print('Массив индексов столбцов содержащих нечетное количество цифр:', arr)