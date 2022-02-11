# Дан бинарный файл удалить простые числа из бинарного файла, можно считать файл в список
import random
import struct

def prime_check(N):
    for i in range(2, N // 2 + 1):
        if N % i == 0:
            return False
    return True

file_name = input('Введите имя файла: ')
f = open(file_name, 'wb+')
for i in range(11):
    f.write(struct.pack('q', random.randint(1, 100)))
f.close()

f = open(file_name, 'rb+')
print('Файл после преобразования')
new = f.read(8)
while new:
    num = int(struct.unpack('q', new)[0])
    print(num)
    new = f.read(8)
f.close()

f = open(file_name, 'rb+')

print()
counter = 0
new = f.read(8)
while new:
    num = int(struct.unpack('q', new)[0])
    if prime_check(num):
        print('Простое числоо ' + str(num))
        old = f.tell()
        read_bytes = f.read(8 * (10 - counter))
        f.seek(old - 8)
        f.write(read_bytes)
        f.truncate()
        f.seek(old - 8)
    counter += 1
    new = f.read(8)
f.close()
print()

f = open(file_name, 'rb+')
print('Файл после преобразования')
new = f.read(8)
while new:
    num = int(struct.unpack('q', new)[0])
    print(num)
    new = f.read(8)
f.close()