def two_sum(num, tar):
    new_arr = []
    n = any([num.count(x) > 1 for x in num])
    for x in num:
        ind = num.index(x)
        z = num.pop(ind)
        for y in num:
            if x + y == tar:
                new_arr.append(x)
            print(x, y, num)
        print('......', z, x, num)
        num.insert(ind, z)
    print(n)
    return ([num.index(x) for x in new_arr], [x for x in range(len(new_arr)) if new_arr[x] == num[x]])[n]


print(two_sum([1, 2, 3, 4, 5], 5))
