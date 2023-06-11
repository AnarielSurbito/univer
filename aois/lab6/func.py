def rows(row):
    print(str(row[0]).center(3), end='|')
    print(row[1].center(15), end='|')
    print(str(row[2]).center(5), end='|')
    print(str(row[3]).center(6), end='|')
    print(str(row[5]).center(5), end='|')
    print(' ' + row[4])


def table(tab):
    print('_' * 121)
    print(' № |     слово     |  V  | H(V) |  C  | определение')
    print(' - |', '-' * 13, '|', '-' * 3, '|', '-' * 4, '|', '-' * 3, '|', '-' * 83)
    for i in range(len(tab)):
        rows(tab[i])
    print(' - |', '-' * 13, '|', '-' * 3, '|', '-' * 4, '|', '-' * 3, '|', '-' * 83)


def find_V(key):
    letter1 = ord(key[0]) - ord('a')
    letter2 = ord(key[1]) - ord('a')
    val = letter1 * 26 + letter2
    return val


def find_H(val):
    addr = val % 20
    return addr


def find_last(tab, addr):
    if tab[addr][5] == '':
        return addr
    else:
        return find_last(tab, tab[addr][5])


def add(tab, key, info):
    val = find_V(key)
    addr = find_H(val)
    if tab[addr][1] == '':
        tab[addr] = [addr, key, val, addr, info, '']
    elif tab[addr][3] != addr:
        key1 = tab[addr][1]
        info1 = tab[addr][1]
        del_row(key1, tab)
        tab[addr] = [addr, key, val, addr, info, '']
        add(tab, key1, info1)
    else:
        ind = 0
        for i in range(len(tab)):
            if tab[i][1] == '':
                ind = i
                break
        last = find_last(tab, addr)
        tab[last][5] = ind
        tab[ind] = [ind, key, val, addr, info, '']


def find_row(key, tab, addr=''):
    if addr == '':
        val = find_V(key)
        addr = find_H(val)
    if tab[addr][1] == key:
        return tab[addr]
    if tab[addr][5] != '':
        return find_row(key, tab, addr=tab[addr][5])
    return None



def del_row(key, tab, addr=''):
    if addr == '':
        val = find_V(key)
        addr = find_H(val)
    if tab[addr][1] == key:
        if tab[addr][5] == '' and addr == tab[addr][3]:
            tab[addr] = [addr, '', '', '', '', '']
        elif tab[addr][5] != '':
            next_ind = tab[addr][5]
            tab[addr] = tab[next_ind]
            tab[addr][0] = addr
            tab[next_ind] = [next_ind, '', '', '', '', '']
        else:
            preV = 0
            for i in range(20):
                if tab[i][5] == addr:
                    preV = i
                    break
            tab[preV][5] = tab[addr][5]
            tab[addr] = [addr, '', '', '', '', '']
    else:
        del_row(key, tab, addr=tab[addr][5])



def menu(tab):
    while True:
        opt = input('\n1 - таблица\n2 - добавить термин\n3 - найти термин\n4 - удалить термин\n')
        match opt:
            case '1':
                table(tab)
            case '2':
                key = input('\nТермин: ')
                if find_row(key, tab) != None:
                    print('Данный термин уже есть')
                else:
                    info = input('Определение: ')
                    add(tab, key, info)
            case '3':
                key = input('\nТермин: ')
                term = find_row(key, tab)
                if term == None:
                    print('Термин не найден')
                else:
                    table([term])
            case '4':
                key = input('\nТермин: ')
                del_row(key, tab)
