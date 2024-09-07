def fun(n=int(input()), m=int(input())):
    arr_1 = list(range(1, n + 1))
    arr_2 = []
    arr_3 = arr_1
    final_num = []
    a, b = 0, m

    while arr_3[-1] != arr_1[0]:
        if m > n:
            print('Второй аргумент должен быть меньше или равен первому.')
            break
        arr_2.extend(arr_1)
        arr_3 = arr_2[a:b]
        new_arr = arr_2[a:b]
        final_num.append(new_arr[0])
        a, b = b - 1, b + m - 1

    return print(''.join([str(x) for x in final_num]))


fun()
