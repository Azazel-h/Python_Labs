from math import cos
def func(x) -> float:
    return 5 + 6 + 1 / cos(x ** 2) + 1 - 100

x_first = float(input('Введите начальное значение: '))
h = float(input('Введите шаг: '))
x_last = float(input('Введите конечное значение: '))
max_f = func(x_first)
min_f = func(x_first)
EPS = 1e-5
GRAPH_W = 80
num_of_h = int((x_last - x_first + EPS) // h)

for i in range(num_of_h + 1):
    x = x_first + h * i
    if (x - x_last > EPS): break
    y = func(x)
    min_f = min(y, min_f)
    max_f = max(y, max_f)

print(' ' * 5, end='')
cut_1 = f'{min_f:.2f}'
cut_2 = f'{max_f:.2f}'
spaces = GRAPH_W - len(cut_1)
for i in range(spaces + 1):
    if i == 0:
        print(cut_1, end='')
    elif i == spaces:
        print(cut_2, end='')
    else:
        print(' ', end='')
print()

print(' ' * 7, end='')
for i in range(GRAPH_W + 1):
    if i == 0 or i == GRAPH_W:
        print('|', end='')
    else:
        print('-', end='')
print('>')

for i in range(num_of_h + 1):
    x = x_first + h * i
    y = func(x)
    normalized_y = (y - min_f) / (max_f - min_f)
    y_position = int(normalized_y * GRAPH_W)
    print(f'{x:>5.2f} |' + (y_position - 1) * ' ' + '*')