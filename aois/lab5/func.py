q1 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
q2 = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
q3 = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
V = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
q1_ = []
q2_ = []
q3_ = []
h1 = [0]
h2 = [0]
h3 = [0]
hfunc = []
atoms = ['q3', 'q2', 'q1', 'V']

def plusone():
    for el in range(len(q1)):
        temp = []
        temp.append(q1[el])
        temp.append(q2[el])
        temp.append(q3[el])
        temp[2] += V[el]
        if temp[2] == 2:
            temp[2] = 0
            temp[1] += 1
        if temp[1] == 2:
             temp[1] = 0
             temp[0] += 1
        if temp[0] == 2:
            temp[0] = 0
        q3_.append(temp[0])
        q2_.append(temp[1])
        q1_.append(temp[2])


def print_q():
    print("q3   ", end='')
    for el in range(len(q3)):
        print(q1[el], end=' ')
    print('')
    print("q2   ", end='')
    for el in range(len(q2)):
        print(q2[el], end=' ')
    print('')
    print("q1   ", end='')
    for el in range(len(q1)):
        print(q3[el], end=' ')
    print('')
    print("V    ", end='')
    for el in range(len(V)):
        print(V[el], end=' ')
    print('')
    print('------------------------------------')
    print("q3*  ", end='')
    for el in range(len(q3)):
        print(q3_[el], end=' ')
    print('')
    print("q2*  ", end='')
    for el in range(len(q2)):
        print(q2_[el], end=' ')
    print('')
    print("q1*  ", end='')
    for el in range(len(q1)):
        print(q1_[el], end=' ')
    print('')


def make_h():
    for el in range(1, len(q1) - 1):
        if (q3[el] == 0 and q3[el + 1] == 1) or (q3[el] == 1 and q3[el + 1] == 0):
            h1.append(1)
        else:
            h1.append(0)
        if (q2[el] == 0 and q2[el + 1] == 1) or (q2[el] == 1 and q2[el + 1] == 0):
            h2.append(1)
        else:
            h2.append(0)
        if (q1[el] == 0 and q1[el + 1] == 1) or (q1[el] == 1 and q1[el + 1] == 0):
            h3.append(1)
        else:
            h3.append(0)
    h1.append(1)
    h2.append(1)
    h3.append(1)


def print_h():
    print("h3   ", end='')
    for el in range(len(q3)):
        print(h3[el], end=' ')
    print('')
    print("h2   ", end='')
    for el in range(len(q2)):
        print(h2[el], end=' ')
    print('')
    print("h1   ", end='')
    for el in range(len(q1)):
        print(h1[el], end=' ')
    print('')


def fun(h):
    var = []
    numb = []
    for el in range(len(h3)):
        temp = ''
        tempvar = ''
        if h[el] == 1:
            if q1[el] == 1:
                temp += '(q3&'
                tempvar += '1'
            elif q1[el] == 0:
                temp += '((!q3)&'
                tempvar += '0'
            if q2[el] == 1:
                temp += 'q2&'
                tempvar += '1'
            elif q2[el] == 0:
                temp += '(!q2)&'
                tempvar += '0'
            if q3[el] == 1:
                temp += 'q1&'
                tempvar += '1'
            elif q3[el] == 0:
                temp += '(!q1)&'
                tempvar += '0'
            if V[el] == 1:
                temp += 'V)v'
                tempvar += '1'
            elif V[el] == 0:
                temp += '(!V))v'
                tempvar += '0'
        if len(temp) > 0:
            hfunc.append(temp)
        if len(tempvar) > 0:
            var.append(tempvar)
    print("func: ", end=' ')
    for el in range(len(hfunc)):
        print(hfunc[el], end='')
    print('')
    answer = []
    ansvar = []
    for el1 in range(len(var) - 1):
        for el2 in range(1, len(var)):
            if not el1 == el2:
                tempans = ''
                tem = ''
                for el_ in range(len(var[el1])):
                    if var[el1][el_] == var[el2][el_]:
                        tempans += str(el_)
                        tem += str(var[el1][el_])
                if len(tempans) > 1:
                    answer.append(tempans)
                    ansvar.append(tem)
    th = '('
    if (h == h3):
        print("T: ", end='')
        for el in range(len(answer)):
            for el_ in range(len(answer[el])):
                if int(ansvar[el][el_]) == 0:
                    th += '(!' + str(atoms[int(answer[el][el_])]) + ')&'
                elif int(ansvar[el][el_]) == 1:
                    th += str(atoms[int(answer[el][el_])]) + '&'
    elif (h == h2):
        ansvar.clear()
        ansvar.append('11')
        answer.clear()
        answer.append('23')
        print("T: ", end='')
        for el in range(len(answer)):
            for el_ in range(len(answer[el])):
                if int(ansvar[el][el_]) == 0:
                    th += '(!' + str(atoms[int(answer[el][el_])]) + ')&'
                elif int(ansvar[el][el_]) == 1:
                    th += str(atoms[int(answer[el][el_])]) + '&'
    elif (h == h1):
        ansvar.clear()
        ansvar.append('1')
        answer.clear()
        answer.append('3')
        print("T: ", end='')
        for el in range(len(answer)):
            for el_ in range(len(answer[el])):
                if int(ansvar[el][el_]) == 0:
                    th += '(!' + str(atoms[int(answer[el][el_])]) + ')&'
                elif int(ansvar[el][el_]) == 1:
                    th += str(atoms[int(answer[el][el_])]) + '&'
    th = th[:-1] + ')'
    print(th)
    th = th.replace('!', '~')
    th = th.replace('v', '+')
    print('For logisim:', end='')
    print(th)
    th = ''
    var.clear()
    numb.clear()
    ansvar.clear()
    answer.clear()
    hfunc.clear()

