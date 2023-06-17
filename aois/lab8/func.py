import random


def tab_hor():
    array = []
    bin = 0, 1
    for _ in range(16):
        line = []
        for _ in range(16):
            line.append(random.choice(bin))
        array.append(line)
    return array


def change_vert(array):
    new = tab_hor()
    for x in range(16):
        for y in range(16):
            new_y = y + x
            if new_y >= 16:
                new_y = y + x - 16
            new[new_y][x] = array[x][y]
    return new


def read_vert(index, array):
    word = []
    for x in range(len(array)):
        diff_x = x + index
        if diff_x >= len(array):
            diff_x -= 16
        word.append(array[diff_x][index])
    return word


def print_list(array: list):
    #print('___________________Таблица______________________')
    for x in range(len(array)):
        print(array[x])


def f6(value1, value2):
    return (not value1 and value2) or (not value2 and value1)


def f9(value1, value2):
    return (value1 and value2) or (not value2 and not value1)


def f4(value1, value2):
    return not value1 and value2


def f11(value1, value2):
    return value1 or not value2


def oper_f4(word1, word2):
    res = []
    for x in range(len(word1)):
        res.append(int(f4(word1[x], word2[x])))
    return res


def oper_f6(word1, word2):
    res = []
    for x in range(len(word1)):
        res.append(int(f6(word1[x], word2[x])))
    return res


def oper_f9(word1, word2):
    res = []
    for x in range(len(word1)):
        res.append(int(f9(word1[x], word2[x])))
    return res


def oper_f11(word1, word2):
    res = []
    for x in range(len(word1)):
        res.append(int(f11(word1[x], word2[x])))
    return res


def log_oper(index1, index2, oper, array):
    if oper == 'f4':
        array[index2] = oper_f4(array[index1], array[index2])
    if oper == 'f9':
        array[index2] = oper_f9(array[index1], array[index2])
    if oper == 'f6':
        array[index2] = oper_f6(array[index1], array[index2])
    if oper == 'f11':
        array[index2] = oper_f11(array[index1], array[index2])


def search(index, array):
    print(array[index])


def setter(index, value, array):
    array[index] = value


def summa(arg1, arg2):
    ans = [0, 0, 0, 0, 0]
    trans = 0
    for x in range(len(arg1) - 1, -1, -1):
        if arg1[x] + arg2[x] + trans == 0:
            ans[x + 1] = 0
        if arg1[x] + arg2[x] == 1:
            if trans == 0:
                ans[x + 1] = 1
            if trans == 1:
                ans[x + 1] = 0
        if arg1[x] + arg2[x] == 2:
            if trans == 1:
                ans[x + 1] = 1
            if trans == 0:
                trans = 1
                ans[x + 1] = 0
    if trans == 1:
        ans[0] = 1
    return ans


def summ(V, array):
    for x in range(len(array)):
        if V[:3] == array[x][:3]:
            word1 = array[x][3:7]
            word2 = array[x][7:11]
            array[x][11:16] = summa(word1, word2)


def search_max(array):
    ans = []
    add = [1 for _ in range(len(array))]
    for x in range(len(array[0])):
        val = 0
        for y in range(len(array)):
            if array[y][x] ==  1 and add[y] == 1:
                val = 1
                break
        for y in range(len(array)):
            if val == 1:
                if array[y][x] != 1:  add[y] = 0
        for y in range(len(array)):
            if val == 1 and add[y] == 1:
                ans.append(1)
                break
            if val == 0 and add[y] == 1:
                ans.append(0)
                break
    return ans


def search_min(array):
    ans = []
    add = [1 for _ in range(len(array))]
    for x in range(len(array[0])):
        val = 1
        for y in range(len(array)):
            if array[y][x] == 0 and add[y] == 1:
                val = 0
                break
        for y in range(len(array)):
            if val == 0:
                if array[y][x] != 0:
                    add[y] = 0
        for y in range(len(array)):
            if val == 0 and add[y] == 1:
                ans.append(0)
                break
            if val == 1 and add[y] == 1:
                ans.append(1)
                break
    return ans


def sort(array: list, flag: str):
    res = []
    arr = array[:]
    if flag == 'min':
        while len(arr) > 0:
            min = search_min(arr)
            res.append(min)
            arr.remove(min)
    if flag == 'max':
        while len(arr) > 0:
            max = search_max(arr)
            res.append(max)
            arr.remove(max)
    return res