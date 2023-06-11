import func as fun

tab = []
for i in range(20):
    tab.append([i, '', '', '', '', ''])
inform = open('inform.txt')
lines = inform.readlines()
coll = []
for el in lines:
    key, info = el.split(' - ')
    info = info.replace('\n', '')
    val = fun.find_V(key)
    address = fun.find_H(val)
    row = [address, key, val, address, info, '']
    if tab[address][1] == '':
        tab[address] = row
    else:
        coll.append(row)
for row in coll:
    fun.add(tab, row[1], row[4])
fun.table(tab)
fun.menu(tab)

