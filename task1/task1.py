import math


def fun(n, m):
    arr = list(range(1, n + 1))
    arr.extend(arr * int(math.ceil(m / n)))
    a, b, c = 0, m, ''
    while True:
        c += str(arr[a:b][0])
        if arr[0] == arr[a:b][-1]:
            return print('Полученый путь: ' + c)
        a = (b - 1) % n
        b = a + m


while True:
    fun(int(input('n = ')), int(input('m = ')))
    if input("Хотите продолжить?(y/n) = ") != 'y':
        break
