def two_sum(num, tar):
    new_arr = []
    for x in num:
        ind = num.index(x)
        z = num.pop(ind)
        for y in num:
            if x + y == tar:
                new_arr.append(x)
            print(x, y, num)
        print('......', z, x, num)
        num.insert(ind, z)
    return [num.index(x) for x in new_arr]


print(two_sum([1, 2, 3], 4))

