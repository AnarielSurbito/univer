abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# (((A&(!B))v(!A))>C)
# ((((P>R)&(Q>S))&((!P)v(!S)))>((!P)v(!Q)))
pseudo = []


rendition = []


atoms = []


answer = []


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


def solution(func):
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
    hav = False
    result: list = answer[len(answer) - 1]
    sknf = []
    for ind in range(len(result)):
        if result[ind] == 0:
            hav = True
            sknf.append("(")
            add_in_sknf(sknf, str(rendition[ind + 1]))
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
    result: list = answer[len(answer) - 1]
    sdnf = []
    hav = False
    for ind in range(len(result)):
        if result[ind] == 1:
            hav = True
            sdnf.append("(")
            add_in_sdnf(sdnf, str(rendition[ind + 1]))
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
