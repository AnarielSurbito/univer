import random


def create_arr(m: int, n: int):
    bin = [0, 1]
    arr = []
    for _ in range(m):
        word = []
        for _ in range(n):
            word.append(random.choice(bin))
        arr.append(word)
    return arr


def get_g_l(g, l, a, s, ind, matches):
    if ind < len(a):
        g = g or (not a[ind] and s[ind] and not l)
        l = l or (a[ind] and not s[ind] and not g)
        if a[ind] == s[ind]:
            matches += 1
        ind += 1
        return get_g_l(g, l, a, s, ind, matches)
    else:
        return g, l, matches


def compare(addr1, addr2, arr):
    if addr1 < len(arr) and addr2 < len(arr):
        matches = 0
        a = arr[addr1]
        s = arr[addr2]
        g, l, matches = get_g_l(0, 0, a, s, 0, matches)
        if g > l:
            print(s, '>', a)
        elif g < l:
            print(s, '<', a)
        elif g == l:
            print(a, '=', a)


def max_min(arr):
    ans = []
    add = [1 for _ in range(len(arr))]
    for x in range(len(arr[0])):
        val = 0
        for y in range(len(arr)):
            if arr[y][x] == 1 and add[y] == 1:
                val = 1
                break
        for y in range(len(arr)):
            if val == 1:
                if arr[y][x] != 1:
                    add[y] = 0
        for y in range(len(arr)):
            if val == 1 and add[y] == 1:
                ans.append(1)
                break
            if val == 0 and add[y] == 1:
                ans.append(0)
                break
    return ans


def min_max(arr):
    ans = []
    add = [1 for _ in range(len(arr))]
    for x in range(len(arr[0])):
        val = 1
        for y in range(len(arr)):
            if arr[y][x] == 0 and add[y] == 1:
                val = 0
                break
        for y in range(len(arr)):
            if val == 0:
                if arr[y][x] != 0:
                    add[y] = 0
        for y in range(len(arr)):
            if val == 0 and add[y] == 1:
                ans.append(0)
                break
            if val == 1 and add[y] == 1:
                ans.append(1)
                break
    return ans


def sort(arr: list, type: str):
    res = []
    arr = arr[:]
    if type == 'min':
        while len(arr) > 0:
            min = min_max(arr)
            res.append(min)
            arr.remove(min)
    if type == 'max':
        while len(arr) > 0:
            max = max_min(arr)
            res.append(max)
            arr.remove(max)
    return res


def search_match(arg, arr):
    ans = 0
    ind = 0
    for x in range(len(arr)):
        _, _, match = get_g_l(0, 0, arg, arr[x], 0, 0)
        if ans < match:
            ans = match
            ind = x
    return ans, ind
