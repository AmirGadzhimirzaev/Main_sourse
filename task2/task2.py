files = ['circle.txt', 'dot.txt']
handles = [open(file) for file in files]


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


fun(handles[0], handles[1])
