def fun(cir_pos, dot_pos):
    circ = [x.split() for x in cir_pos.readlines()]
    dot = [x.split() for x in dot_pos.readlines()]
    for dot_data in dot:
        result = ((int(dot_data[0]) - int(circ[0][0])) ** 2 / int(circ[1][0]) ** 2
                  + (int(dot_data[1]) - int(circ[0][1])) ** 2 / int(circ[1][0]) ** 2)

        if result < 1:
            print(1)
        elif result == 1:
            print(0)
        else:
            print(2)


while True:
    try:
        with open(input()) as f_1, open(input()) as f_2:
            fun(f_1, f_2)
    except IOError as e:
        print('Operation failed: %s' % e.strerror)
    if input('Хотите повторить?(y/n) ') != 'y':
        break
