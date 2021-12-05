def f(x):
    return x ** 2

def F(x):
    return (x ** 3) / 3

def trapezoidal_rule(N, start, end):
    S = 0
    step = (end - start) / N
    start_temp = start
    end_temp = start + step
    for i in range(N):
        S += (end_temp - start_temp) * (f(start_temp) + f(end_temp)) / 2
        start_temp = end_temp
        end_temp += step
    return S

start = float(input('Введите начало отрезка: '))
end = float(input('Введите конец отрезка: '))
N = int(input('Введите количество разбиений: '))

real_integral = F(end) - F(start)
trapezoidal = trapezoidal_rule(N, start, end)
print('Реальное значение интеграла:', real_integral)
print('Интеграл методом трапеции:', trapezoidal)
print(f'Относительная погрешность: {abs((trapezoidal - real_integral) / real_integral) * 100:.5f} %')