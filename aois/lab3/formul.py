abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


pseudo = []


rendition = []


atoms = []


answer = []


Sknf = []


Sdnf = []


def belong_abc(el: str):
    for atom in abc:
        if el == atom:
            return True
    return False


def list_atoms(form: str):
    global atoms
    for el in form:
        if belong_abc(el):
            atoms.append(el)
    atoms = sorted(list(set(atoms)))


def create_rendition():
    global rendition
    global atoms
    rendition.append(atoms)
    for ind in range(2 ** len(atoms)):
        rendition.append(format(ind, 'b'))
    for ind, el in enumerate(rendition):
        if not len(el) == len(atoms):
            rendition[ind] = '0' * (len(atoms) - len(el)) + el


# (((A&(!B))v(!A))>C)
def conversion(form: str):
    iterat_number = 0
    for el in form:
        if el == '(':
            iterat_number += 1
    while iterat_number:
        form = change_form(form)
        iterat_number -= 1


def change_form(form: str):
    for ind, el in enumerate(form):
        if el == '(':
            ind_close = close_parenthesis(form, ind)
            if ind_close:
                pseudo.append(form[ind:ind_close] + ')')
                form = form.replace(form[ind:ind_close] + ')', str(len(pseudo)), 1)
                return form


def close_parenthesis(form: str, ind_open_parenthesis: int):
    for ind in range(ind_open_parenthesis + 1, len(form)):
        if form[ind] == '(':
            return 0
        if form[ind] == ')':
            return ind
    return False


def check_brack(func):
    op_brack = 0
    close_brack = 0
    for el in func:
        if el == '(':
            op_brack += 1
        elif el == ')':
            close_brack += 1
    if op_brack == close_brack:
        return True
    elif not op_brack == close_brack:
        return False


def solution(func):
    if not check_brack(func):
        return False
    list_atoms(func)
    create_rendition()
    conversion(func)
    global pseudo
    global answer
    for el in pseudo:
        temp = []
        if el[1] == '!':
            list1 = unary(el[2])
            for el_ in range(len(list1)):
                if solve(int(list1[el_]), '!'):
                    temp.append(1)
                else:
                    temp.append(0)
            answer.append(temp)
        else:
            list1 = binary(el[1])
            list2 = binary(el[3])
            for el_ in range(len(list1)):
                temp.append(solve(int(list1[el_]), el[2], int(list2[el_])))
            answer.append(temp)


def unary(el):
    if belong_abc(el):
        list_ = atoms_val(atoms.index(el))
        return list_
    elif el.isdigit():
        list_ = answer[int(el) - 1]
        return list_


def binary(el):
    if belong_abc(el):
        list_ = atoms_val(atoms.index(el))
        return list_
    elif el.isdigit():
        list_ = answer[int(el) - 1]
        return list_


def solve(first: int, connect: str, second: int = 0):
    if connect == '!':
        return not first
    if connect == '&':
        return first & second
    if connect == 'v':
        return first or second
    if connect == '~':
        return first == second
    if connect == '>':
        if first == 1 and second == 0:
            return 0
        else:
            return 1


def atoms_val(ind: int):
    global rendition
    result = []
    for el in range(1, len(rendition)):
        result.append(rendition[el][ind])
    return result


def SKNF():
    global rendition
    global atoms
    global Sknf
    hav = False
    result: list = answer[len(answer) - 1]
    sknf = []
    for ind in range(len(result)):
        if result[ind] == 0:
            hav = True
            sknf.append("(")
            add_in_sknf(sknf, str(rendition[ind + 1]))
            Sknf.append(rendition[ind + 1])
            if ind == len(result) - 1:
                sknf.append(")")
            elif not ind == len(result) - 1:
                sknf.append(")&\n")
    var = ''.join(sknf)
    if hav:
        if var[-1] == '&':
            var = var[:-1]
    print(var)


def add_in_sknf(sknf: list, numbs: str):
    for ind, atom in enumerate(numbs):
        if atom == '0':
            sknf.append(atoms[ind])
            if not ind == len(numbs) - 1:
                sknf.append("v")
        elif atom == '1':
            sknf.append('(!' + atoms[ind])
            if not ind == len(numbs) - 1:
                sknf.append(")v")
            elif ind == len(numbs) - 1:
                sknf.append(")")



def SDNF():
    global rendition
    global atoms
    global Sdnf
    result: list = answer[len(answer) - 1]
    sdnf = []
    hav = False
    for ind in range(len(result)):
        if result[ind] == 1:
            hav = True
            sdnf.append("(")
            add_in_sdnf(sdnf, str(rendition[ind + 1]))
            Sdnf.append(rendition[ind+1])
            if ind == len(result) - 1:
                sdnf.append(")")
            elif not ind == len(result) - 1:
                sdnf.append(")v\n")
    var = ''.join(sdnf)
    if hav:
        if var[-1] == 'v':
            var = var[:-1]
    print(var)


def add_in_sdnf(sdnf: list, numbs: str):
    for ind, atom in enumerate(numbs):
        if atom == '1':
            sdnf.append(atoms[ind])
            if not ind == len(numbs) - 1:
                sdnf.append("&")
        elif atom == '0':
            sdnf.append('(!' + atoms[ind])
            if ind < len(numbs) - 1:
                sdnf.append(")&")
            elif ind == len(numbs) - 1:
                sdnf.append(")")



def get_info():
    global rendition
    global answer
    print(rendition[0])
    for el in range(len(answer)):
        print(el+1, pseudo[el], answer[el], sep='\t')
    print('')


#Расчётный метод
def sKNF():
    global Sknf
    var: list = []
    numb: list = []
    ssknf: list = []
    i = 0
    for el1 in range(len(Sknf) - 1):
        for el2 in range(1 + i, len(Sknf)):
            j = 0
            for ind1 in range(len(atoms) - 1):
                for ind2 in range(1 + j, len(atoms)):
                    if Sknf[el1][ind1] == Sknf[el2][ind1] and not ind1 == ind2:
                        if Sknf[el1][ind2] == Sknf[el2][ind2]:
                            temp: str = str(Sknf[el1][ind1]) + str(Sknf[el1][ind2])
                            var.append(temp)
                            tempNumb: str = str(ind1 + 1) + str(ind2 + 1)
                            numb.append(tempNumb)
                j += 1
        i += 1
    for el in range(len(var)):
        temp: str = '('
        if int(var[el][0]) == 1:
            temp += '(!' + atoms[int(numb[el][0]) - 1] + ')'
        elif int (var[el][0]) == 0:
            temp += atoms[int(numb[el][0]) - 1]
        temp += 'v'
        if int(var[el][1]) == 1:
            temp += '(!' + atoms[int(numb[el][1]) - 1] + ')'
        elif int (var[el][1]) == 0:
            temp += atoms[int(numb[el][1]) - 1]
        temp += ')&'
        ssknf.append(temp)
    for el in range(len(ssknf)):
        print(ssknf[el], end='')
    print('')
    TKNF(numb, var)
    print('end')
    print("")
    RSHKNF(numb, var)
    print('end')


def sDNF():
    global Sdnf
    var: list = []
    numb: list = []
    ssdnf: list = []
    i = 0
    for el1 in range(len(Sdnf) - 1):
        for el2 in range(1 + i, len(Sdnf)):
            j = 0
            for ind1 in range(len(atoms) - 1):
                for ind2 in range(1 + j, len(atoms)):
                    if Sdnf[el1][ind1] == Sdnf[el2][ind1] and not ind1 == ind2:
                        if Sdnf[el1][ind2] == Sdnf[el2][ind2]:
                            temp: str = str(Sdnf[el1][ind1]) + str(Sdnf[el1][ind2])
                            var.append(temp)
                            tempNumb: str = str(ind1 + 1) + str(ind2 + 1)
                            numb.append(tempNumb)
                j += 1
        i += 1
    for el in range(len(var)):
        temp: str = '('
        if int(var[el][0]) == 0:
            temp += '(!' + atoms[int(numb[el][0]) - 1] + ')'
        elif int(var[el][0]) == 1:
            temp += atoms[int(numb[el][0]) - 1]
        temp += '&'
        if int(var[el][1]) == 0:
            temp += '(!' + atoms[int(numb[el][1]) - 1] + ')'
        elif int(var[el][1]) == 1:
            temp += atoms[int(numb[el][1]) - 1]
        temp += ')v'
        ssdnf.append(temp)
    for el in range(len(ssdnf)):
        print(ssdnf[el], end='')
    print('')
    TDNF(numb, var)
    print('end')
    print('')
    RSHDNF(numb, var)
    print('end')


def TKNF(numb: list, var: list):
    tknf: list = []
    i = 0
    tnumb = []
    tvar = []
    for el in range(len(numb)):
        tnumb.append(numb[el])
    for el in range(len(var)):
        tvar.append(var[el])
    tnumb, tvar = check_double(tnumb, tvar)
    for el1 in range(len(tnumb)):
        for el2 in range(len(tnumb)):
            if el1 < len(tnumb) and el2 < len(tnumb) and tnumb[el1] == tnumb[el2] and not el1 == el2:
                tnumb.pop(el2)
                tvar.pop(el2)
    for el in range(len(var)):
        temp = addTKNF(el, tnumb, tvar)
        tknf.append(temp)
    for el in range(len(tknf)):
        print(tknf[el], end='')
    print('')


def addTKNF(el: int, numb: list, var: list):
    temp: str = '('
    if numb[el][0] == '-' and not numb[el][2] == '-':
        if int(var[el][1]) == 1:
            temp += '(!' + atoms[int(numb[el][2]) - 1] + ')'
        elif int(var[el][1]) == 0:
            temp += atoms[int(numb[el][2]) - 1]
    elif not numb[el][0] == '-' and numb[el][1] == '-':
        if int(var[el][0]) == 1:
            temp += '(!' + atoms[int(numb[el][0]) - 1] + ')'
        elif int(var[el][0]) == 0:
            temp += atoms[int(numb[el][0]) - 1]
    elif not numb[el][0] == '-' and not numb[el][1] == '-':
        if int(var[el][0]) == 1:
            temp += '(!' + atoms[int(numb[el][0]) - 1] + ')'
        elif int(var[el][0]) == 0:
            temp += atoms[int(numb[el][0]) - 1]
        temp += 'v'
        if int(var[el][1]) == 1:
            temp += '(!' + atoms[int(numb[el][1]) - 1] + ')'
        elif int(var[el][1]) == 0:
            temp += atoms[int(numb[el][1]) - 1]
    temp += ')&'
    return temp


def TDNF(numb: list, var: list):
    tdnf: list = []
    i = 0
    tnumb = []
    tvar = []
    for el in range(len(numb)):
        tnumb.append(numb[el])
    for el in range(len(var)):
        tvar.append(var[el])
    tnumb, tvar = check_double(tnumb, tvar)
    for el1 in range(len(tnumb)):
        for el2 in range(len(tnumb)):
            if el1 < len(tnumb) and el2 < len(tnumb) and tnumb[el1] == tnumb[el2] and not el1 == el2:
                tnumb.pop(el2)
                tvar.pop(el2)
    for el in range(len(tvar)):
        temp = addTDNF(el, tnumb, tvar)
        tdnf.append(temp)
    for el in range(len(tdnf)):
        print(tdnf[el], end='')
    print('')


def addTDNF(el, numb: list, var: list):
    temp: str = '('
    if numb[el][0] == '-' and not numb[el][2] == '-':
        if int(var[el][1]) == 0:
            temp += '(!' + atoms[int(numb[el][2]) - 1] + ')'
        elif int(var[el][1]) == 1:
            temp += atoms[int(numb[el][2]) - 1]
    elif not numb[el][0] == '-' and numb[el][1] == '-':
        if int(var[el][0]) == 0:
            temp += '(!' + atoms[int(numb[el][0]) - 1] + ')'
        elif int(var[el][0]) == 1:
            temp += atoms[int(numb[el][0]) - 1]
    elif not numb[el][0] == '-' and not numb[el][1] == '-':
        if int(var[el][0]) == 0:
            temp += '(!' + atoms[int(numb[el][0]) - 1] + ')'
        elif int(var[el][0]) == 1:
            temp += atoms[int(numb[el][0]) - 1]
        temp += '&'
        if int(var[el][1]) == 0:
            temp += '(!' + atoms[int(numb[el][1]) - 1] + ')'
        elif int(var[el][1]) == 1:
            temp += atoms[int(numb[el][1]) - 1]
    temp += ')v'
    return temp


# Расчётно-табличный метод
def RSHDNF(numb: list, var: list):
    global Sdnf
    i = 0
    table = []
    answ = []
    rtnumb = []
    rtvar = []
    print("Расчётно-табличный метод для СДНФ")
    for el in range(len(numb)):
        rtnumb.append(numb[el])
    for el in range(len(var)):
        rtvar.append(var[el])
    while i < len(numb):
        j = 0
        temp = []
        while j < len(Sdnf):
            temp.append(0)
            j += 1
        table.append(temp)
        i += 1
    i = 0
    while i < len(numb):
        j = 0
        temp = []
        while j < len(Sdnf):
            temp.append(0)
            j += 1
        answ.append(temp)
        i += 1
    for el1 in range(len(var)):
        for el2 in range(len(Sdnf)):
            if rtvar[el1][0] == Sdnf[el2][int(numb[el1][0]) - 1] and rtvar[el1][1] == Sdnf[el2][int(numb[el1][1]) - 1]:
                table[el1][el2] = 1
    for el in range(len(table)):
        for el1 in range(len(table[el])):
            print(table[el][el1], end='')
        print('')
    leng = len(table[0])
    j = 0
    while j < len(table):
        check_one = [0 for k in range(leng)]
        el1 = 0
        while el1 < leng: # проходим по элементам каждого списка 1-0
            for el in range(len(table)): # по каждому списку из списка
                if not el == j:
                    if table[el][el1] == 1:
                        check_one[el1] = 1
            el1 += 1
        ones = 0
        for el in range(len(check_one)):
            if check_one[el] == 1:
                ones += 1
        if ones == len(check_one):
            table.pop(j)
            rtvar.pop(j)
            rtnumb.pop(j)
        check_one.clear()
        j += 1
    print('')
    for el in range(len(table)):
        for el1 in range(len(table[el])):
            print(table[el][el1], end='')
        print('')
    rtnumb, rtvar = check_double(rtnumb, rtvar)
    rtdnf = []
    for el in range(len(rtvar)):
        temp = addTDNF(el, rtnumb, rtvar)
        rtdnf.append(temp)
    for el in range(len(rtdnf)):
        print(rtdnf[el], end='')
    print('')


def check_double(numb: list, var: list):
    for el1 in range(len(numb)):
        for el2 in range(len(numb)):
            if el1 < len(numb) and el2 < len(numb) and numb[el1] == numb[el2] and not el1 == el2:
                if var[el1][0] == var[el2][0] and not var[el1][1] == var[el2][1]:
                    numb[el1] = numb[el1][0] + '-1'
                elif var[el1][1] == var[el2][1] and not var[el1][0] == var[el2][0]:
                    char: str = numb[el1][1]
                    numb[el1] = '-1' + char
                numb.pop(el2)
                var.pop(el2)
    return numb, var


def check_ans(answ: list):
    ones = []
    one = 0
    for el in range(len(answ[0])):
        ones.append(0)
    for el in range(len(answ)):
        for i in range(len(answ[el])):
            if answ[el][i] == 1 and ones[i] == 0:
                ones[i] = 1
                one += 1
    if one == len(answ[0]):
        return True
    else:
        return False


def RSHKNF(numb: list, var: list):
    print("Расчётно-табличный метод для СКНФ")
    global Sknf
    i = 0
    table = []
    answ = []
    rtnumb = []
    rtvar = []
    for el in range(len(numb)):
        rtnumb.append(numb[el])
    for el in range(len(var)):
        rtvar.append(var[el])
    while i < len(numb):
        j = 0
        temp = []
        while j < len(Sknf):
            temp.append(0)
            j += 1
        table.append(temp)
        i += 1
    i = 0
    while i < len(numb):
        j = 0
        temp = []
        while j < len(Sknf):
            temp.append(0)
            j += 1
        answ.append(temp)
        i += 1
    for el1 in range(len(var)):
        for el2 in range(len(Sknf)):
            if rtvar[el1][0] == Sknf[el2][int(numb[el1][0]) - 1] and rtvar[el1][1] == Sknf[el2][int(numb[el1][1]) - 1]:
                table[el1][el2] = 1
    for el in range(len(table)):
        for el1 in range(len(table[el])):
            print(table[el][el1], end='')
        print('')
    leng = len(table[0])
    j = 0
    while j < len(table):
        check_one = [0 for k in range(leng)]
        el1 = 0
        while el1 < leng: # проходим по элементам каждого списка 1-0
            for el in range(len(table)): # по каждому списку из списка
                if not el == j:
                    if table[el][el1] == 1:
                        check_one[el1] = 1
            el1 += 1
        ones = 0
        for el in range(len(check_one)):
            if check_one[el] == 1:
                ones += 1
        if ones == len(check_one):
            table.pop(j)
            rtvar.pop(j)
            rtnumb.pop(j)
        check_one.clear()
        j += 1
    print('')
    for el in range(len(table)):
        for el1 in range(len(table[el])):
            print(table[el][el1], end='')
        print('')
    rtnumb, rtvar = check_double(rtnumb, rtvar)
    rtknf = []
    for el in range(len(rtvar)):
        temp = addTKNF(el, rtnumb, rtvar)
        rtknf.append(temp)
    for el in range(len(rtknf)):
        print(rtknf[el], end='')
    print('')


# Табличный метод
def tabsknf():
    global interpret
    global Sknf
    table = [[' ', '00 ', '01 ', '11 ', '10 '], ['1 ', 0, 0, 0, 0], ['0 ', 0, 0, 0, 0]]
    for el1 in range(len(Sknf)):
        if Sknf[el1][0] == '0':
            if Sknf[el1][1:] == '00':
                table[1][1] = 1
            elif Sknf[el1][1:] == '01':
                table[1][2] = 1
            elif Sknf[el1][1:] == '10':
                table[1][4] = 1
            elif Sknf[el1][1:] == '11':
                table[1][3] = 1
        elif Sknf[el1][0] == '1':
            if Sknf[el1][1:] == '00':
                table[2][1] = 1
            elif Sknf[el1][1:] == '01':
                table[2][2] = 1
            elif Sknf[el1][1:] == '10':
                table[2][4] = 1
            elif Sknf[el1][1:] == '11':
                table[2][3] = 1
    for el1 in range(len(table)):
        for el2 in range(len(table[el1])):
            print(table[el1][el2], end='')
        print('')
    var: list = []
    numb: list = []
    ssknf: list = []
    i = 0
    for el1 in range(len(Sknf) - 1):
        for el2 in range(1 + i, len(Sknf)):
            j = 0
            for ind1 in range(len(atoms) - 1):
                for ind2 in range(1 + j, len(atoms)):
                    if Sknf[el1][ind1] == Sknf[el2][ind1] and not ind1 == ind2:
                        if Sknf[el1][ind2] == Sknf[el2][ind2]:
                            temp: str = str(Sknf[el1][ind1]) + str(Sknf[el1][ind2])
                            var.append(temp)
                            tempNumb: str = str(ind1 + 1) + str(ind2 + 1)
                            numb.append(tempNumb)
                j += 1
        i += 1
    for el in range(len(var)):
        temp: str = '('
        if int(var[el][0]) == 1:
            temp += '(!' + atoms[int(numb[el][0]) - 1] + ')'
        elif int (var[el][0]) == 0:
            temp += atoms[int(numb[el][0]) - 1]
        temp += 'v'
        if int(var[el][1]) == 1:
            temp += '(!' + atoms[int(numb[el][1]) - 1] + ')'
        elif int (var[el][1]) == 0:
            temp += atoms[int(numb[el][1]) - 1]
        temp += ')&'
        ssknf.append(temp)
    for el in range(len(ssknf)):
        print(ssknf[el], end='')
    print("")
    TKNF(numb, var)
    print('end')
    # for el1 in range(1, len(table)):
    #     for el2 in range(1, len(table[el1])):
    #         if table[el1][el2] == 1:
    #             if el1 == 1 and el2 == 1:
    #                 if table[el1 + 1][el2] == 1:
    #                     temps, ans = sokr(str(table[el1][0] + table[0][el2]), str(table[el1 + 1][0] + table[0][el2]))
    #                     answer.append(ans)
    #             if el1 == 2:


def sokr(trip1: str, trip2: str):
    temp = ''
    for el1 in range(trip1):
        for el2 in range(trip2):
            if trip1[el1] == trip2[el2] and not el1 == el2:
                temp = str(trip1[el1]) + str(trip2[el2])
                ans = str(el1) + str(el2)
    return temp, ans


def tabsdnf():
    global interpret
    global Sdnf
    table = [[' ', '00 ', '01 ', '11 ', '10 '], ['1 ', 0, 0, 0, 0], ['0 ', 0, 0, 0, 0]]
    for el1 in range(len(Sdnf)):
        if Sdnf[el1][0] == '0':
            if Sdnf[el1][1:] == '00':
                table[1][1] = 1
            elif Sdnf[el1][1:] == '01':
                table[1][2] = 1
            elif Sdnf[el1][1:] == '10':
                table[1][4] = 1
            elif Sdnf[el1][1:] == '11':
                table[1][3] = 1
        elif Sdnf[el1][0] == '1':
            if Sdnf[el1][1:] == '00':
                table[2][1] = 1
            elif Sdnf[el1][1:] == '01':
                table[2][2] = 1
            elif Sdnf[el1][1:] == '10':
                table[2][4] = 1
            elif Sdnf[el1][1:] == '11':
                table[2][3] = 1
    for el1 in range(len(table)):
        for el2 in range(len(table[el1])):
            print(table[el1][el2], end='')
        print('')
        var: list = []
        numb: list = []
        ssdnf: list = []
        i = 0
        for el1 in range(len(Sdnf) - 1):
            for el2 in range(1 + i, len(Sdnf)):
                j = 0
                for ind1 in range(len(atoms) - 1):
                    for ind2 in range(1 + j, len(atoms)):
                        if Sdnf[el1][ind1] == Sdnf[el2][ind1] and not ind1 == ind2:
                            if Sdnf[el1][ind2] == Sdnf[el2][ind2]:
                                temp: str = str(Sdnf[el1][ind1]) + str(Sdnf[el1][ind2])
                                var.append(temp)
                                tempNumb: str = str(ind1 + 1) + str(ind2 + 1)
                                numb.append(tempNumb)
                    j += 1
            i += 1
    for el in range(len(var)):
        temp: str = '('
        if int(var[el][0]) == 0:
            temp += '(!' + atoms[int(numb[el][0]) - 1] + ')'
        elif int(var[el][0]) == 1:
            temp += atoms[int(numb[el][0]) - 1]
        temp += '&'
        if int(var[el][1]) == 0:
            temp += '(!' + atoms[int(numb[el][1]) - 1] + ')'
        elif int(var[el][1]) == 1:
            temp += atoms[int(numb[el][1]) - 1]
        temp += ')v'
        ssdnf.append(temp)
    for el in range(len(ssdnf)):
        print(ssdnf[el], end='')
    print('')
    TDNF(numb, var)
