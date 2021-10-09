from math import factorial
def func(x, n) -> float:
    return (x ** n) / factorial(n)

x = float(input('Введите X: '))
EPS = float(input('Введите эпсилон: '))
end = int(input('Введите конечное количество итераций: '))
sum = 0
current = 1

while current <= end:
    new_x = func(x, current)
    sum += new_x
    print(f'{current} - {new_x} - {sum:.5f}')
    if abs(new_x) <= EPS:
        print(f'Сумма ряда - {sum:.5f}')
        exit(-1)
    current += 1
print(f'Не удалось достичь нужной точности. Всего итераций: {end}')