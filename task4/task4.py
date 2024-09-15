def fun(numbers):
    nums = [int(x) for x in numbers.readlines()]
    min_sum = []
    for n in nums:
        min_sum.append(sum([abs(n - x) for x in nums if n != x]))
    return print('Минимальное число ходов: ', min(min_sum), '\n')


while True:
    try:
        with open(input('Enter path: ')) as num:
            fun(num)
    except IOError as e:
        print('Operation filed: %s' % e.strerror)
    if input('Хотите повторить?(y/n) ') != 'y':
        break
