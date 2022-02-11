# Булгаков Арсений Сергеевич ИУ7-16Б

import time
import random
from typing import List
from Functions import *

def shell_sort(data: List[int]) -> None:
    """
    Реализация сортировки Шелла
    :param data: Список
    :return:
    """
    last_index = len(data) - 1
    step = len(data) // 2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2

def shell_sort_sorted(N: int) -> float:
    """
    Сортировка отсортированного списка
    :param N: Размерность списка
    :return: Время работы сортировки
    """
    sorted = [i for i in range(3 * (10 ** 18), 2 * (10 ** 18), -((3 * (10 ** 18) - 2 * (10 ** 18)) // N))]
    start_time = time.time()
    shell_sort(sorted)
    return time.time() - start_time

def shell_sort_random(N: int) -> float:
    """
    Сортировка случайного списка
    :param N: Размерность списка
    :return: Время работы сортировки
    """
    random_list = random.sample(range(2 * (10 ** 18), 3 * (10 ** 18)), N)
    start_time = time.time()
    shell_sort(random_list)
    return time.time() - start_time

def shell_sort_reverse_sorted(N: int) -> float:
    """
    Сортировка обратного отсортированного списка
    :param N: Размерность списка
    :return: Время работы сортировки
    """
    reverse_sorted = [i for i in range(2 * (10 ** 18), 3 * (10 ** 18), (3 * (10 ** 18) - 2 * (10 ** 18)) // N)]
    start_time = time.time()
    shell_sort(reverse_sorted)
    return time.time() - start_time


arr = array_validation(input(f'Задайте список для демонстрации работы метода сортировки (Через пробел): ').split(), int)
while str(arr)[0] == 'F':
    arr = array_validation(input(f'Задайте список для демонстрации работы метода сортировки (Через пробел): ').split(), int)

shell_sort(arr)
print(f'Отсортированный список: {arr}')
print('- Введите размерности списков для демонстрации работы метода сортировки Шелла -')

N1 = validation(input('N1: '), int)
while str(N1)[0] == 'F' or int(N1) <= 0:
    if str(N1)[0] == 'F':
        print('Ошибка! - Введите значение типа Int')
    elif int(N1) <= 0:
        print('Ошибка! - Введите значение больше нуля')
    N1 = validation(input('N1: '), int)

N2 = validation(input('N2: '), int)
while str(N2)[0] == 'F' or int(N2) <= 0:
    if str(N2)[0] == 'F':
        print('Ошибка! - Введите значение типа Int')
    elif int(N2) <= 0:
        print('Ошибка! - Введите значение больше нуля')
    N2 = validation(input('N2: '), int)

N3 = validation(input('N3: '), int)
while str(N3)[0] == 'F' or int(N3) <= 0:
    if str(N3)[0] == 'F':
        print('Ошибка! - Введите значение типа Int')
    elif int(N3) <= 0:
        print('Ошибка! - Введите значение больше нуля')
    N3 = validation(input('N3: '), int)

print('- Таблица для сравнения времени сортировки на разных списках -')
print('-' * 75)
print(f'|{"":^34}|{"N1":^12}|{"N2":^12}|{"N3":^12}|')
print(f'|{"Упорядоченный список":^34}|{shell_sort_sorted(N1):>11.6f} |{shell_sort_sorted(N2):>11.6f} |{shell_sort_sorted(N3):>11.6f} |')
print(f'|{"Случайный список":^34}|{shell_sort_random(N1):>11.6f} |{shell_sort_random(N2):>11.6f} |{shell_sort_random(N3):>11.6f} |')
print(f'|{"Упорядоченный в обратном порядке":^34}|{shell_sort_reverse_sorted(N1):>11.6f} |{shell_sort_reverse_sorted(N2):>11.6f} |{shell_sort_reverse_sorted(N3):>11.6f} |')
print('-' * 75)
