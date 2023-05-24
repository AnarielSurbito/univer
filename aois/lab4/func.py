x1 = [0, 0, 0, 0, 1, 1, 1, 1]
x2 = [0, 0, 1, 1, 0, 0, 1, 1]
x3 = [0, 1, 0, 1, 0, 1, 0, 1]
d = [0, 1, 1, 0, 1, 0, 0, 1]
b = [0, 1, 1, 1, 0, 0, 0, 1]

atoms = ['x1', 'x2', 'x3']
atoms2 = ['x1', 'x2', 'x3', 'x4']

bsknf = []
dsknf = []

bvar = []
dvar = []

def table():
    global x1
    global x2
    global x3
    global b
    global d
    print("x1", end='   ')
    for el in x1:
        print(el, sep=' ', end=' ')
    print('')
    print("x2", end='   ')
    for el in x2:
        print(el, sep=' ', end=' ')
    print('')
    print("x3", end='   ')
    for el in x3:
        print(el, sep=' ', end=' ')
    print('')
    print("d", end='    ')
    for el in d:
        print(el, sep=' ', end=' ')
    print('')
    print("b", end='    ')
    for el in b:
        print(el, sep=' ', end=' ')
    print('')


def find_sknf():
    global bsknf
    global dsknf
    global bvar
    global dvar
    for el in range(8):
        if b[el] == 1:
            temps = '('
            tempv = ''
            if x1[el] == 1:
                temps += 'x1&'
                tempv += '1'
            elif x1[el] == 0:
                temps += '(!x1)&'
                tempv += '0'
            if x2[el] == 1:
                temps += 'x2&'
                tempv += '1'
            elif x2[el] == 0:
                temps += '(!x2)&'
                tempv += '0'
            if x3[el] == 1:
                temps += 'x3)'
                tempv += '1'
            elif x3[el] == 0:
                temps += '(!x3))'
                tempv += '0'
            bvar.append(tempv)
            bsknf.append(temps)
        if d[el] == 1:
             temps = '('
             tempv = ''
             if x1[el] == 1:
                temps += 'x1&'
                tempv += '1'
             elif x1[el] == 0:
                 temps += '(!x1)&'
                 tempv += '0'
             if x2[el] == 1:
                 temps += 'x2&'
                 tempv += '1'
             elif x2[el] == 0:
                 temps += '(!x2)&'
                 tempv += '0'
             if x3[el] == 1:
                 temps += 'x3)v'
                 tempv += '1'
             elif x3[el] == 0:
                 temps += '(!x3))v'
                 tempv += '0'
             dvar.append(tempv)
             dsknf.append(temps)
    print('d', end='    ')
    for el in range(len(dsknf)):
        print(dsknf[el], end='')
    print('')
    print('b', end='    ')
    for el in range(len(bsknf)):
        print(bsknf[el], end='')
    print('')


def tknf():
    global dsknf
    global dvar
    global bsknf
    global bvar
    dnumb = []
    bnumb = []
    ssdsknf = []
    ssbsknf = []
    tdsknf = []
    tbsknf = []
    i = 0
    print('d')
    for el1 in range(len(dvar) - 1):
        for el2 in range(1 + i, len(dvar)):
            for ind1 in range(2):
                for ind2 in range(1, 3):
                    if dvar[el1][ind1] == dvar[el2][ind1] and not ind1 == ind2:
                        if dvar[el1][ind2] == dvar[el2][ind2]:
                            temp: str = str(dvar[el1][ind1]) + str(dvar[el1][ind2])
                            ssdsknf.append(temp)
                            tempNumb: str = str(ind1 + 1) + str(ind2 + 1)
                            dnumb.append(tempNumb)
        i += 1
    if len(ssdsknf) == 0:
        ssdsknf = dvar
        for el in range(4):
            dnumb.append('123')
    for el in range(len(ssdsknf)):
        print(ssdsknf[el], end=' ')
    print('')
    for el in range(len(dnumb)):
        print(dnumb[el], end=' ')
    print('')
    print('')
    i = 0
    logisim(dnumb, ssdsknf)
    print('')
    print('b')
    for el1 in range(len(bvar) - 1):
        for el2 in range(1 + i, len(bvar)):
            j = 0
            for ind1 in range(2):
                for ind2 in range(1, 3):
                    if bvar[el1][ind1] == bvar[el2][ind1] and not ind1 == ind2:
                        arg2 = bvar[el2]
                        arg1 = bvar[el1]
                        if arg1[ind2] == arg2[ind2]:
                            temp: str = str(bvar[el1][ind1]) + str(bvar[el1][ind2])
                            ssbsknf.append(temp)
                            tempNumb: str = str(ind1 + 1) + str(ind2 + 1)
                            bnumb.append(tempNumb)
        i += 1
    for el in range(len(ssbsknf)):
        print(ssbsknf[el], end=' ')
    print('')
    for el in range(len(bnumb)):
        print(bnumb[el], end=' ')
    print('')
    print('')
    logisim(bnumb, ssbsknf)


def logisim(numb, ssknf):
    Tknf = ''
    for el in range(len(ssknf)):
        temp: str = '('
        for el1 in range(len(ssknf[el])):
            if int(ssknf[el][el1]) == 0:
                temp += '(!' + atoms[int(numb[el][el1]) - 1] + ')'
            elif int(ssknf[el][el1]) == 1:
                temp += atoms[int(numb[el][el1]) - 1]
            if not el1 == len(ssknf[el]) - 1:
                temp += '&'
        Tknf += temp + ')'
        if not el == len(ssknf) - 1:
            Tknf += 'v'
    print('ТКНФ: ' + Tknf)
    Tknf = Tknf.replace('!', '~')
    Tknf = Tknf.replace('v', '+')
    print('ТКНФ для logisim: ' + Tknf)


def table2():
    plus = plus_5()
    arguments = {1: [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                 2: [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                 3: [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
                 4: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}
    print('\nЗадание 2.')
    print('x1: ' + ' '.join(str(el) for el in arguments[1]))
    print('x2: ' + ' '.join(str(el) for el in arguments[2]))
    print('x3: ' + ' '.join(str(el) for el in arguments[3]))
    print('x4: ' + ' '.join(str(el) for el in arguments[4]))
    print('-----------------------------------')
    print('x1: ' + ' '.join(str(el) for el in plus[0]))
    print('x2: ' + ' '.join(str(el) for el in plus[1]))
    print('x3: ' + ' '.join(str(el) for el in plus[2]))
    print('x4: ' + ' '.join(str(el) for el in plus[3]))


def plus_5():
    five_in_binary_system = [0, 1, 0, 1]
    arguments = {1: [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                 2: [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                 3: [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
                 4: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}
    rezult = [[0 for column in range(len(arguments[1]))] for string in range(4)]
    for i in range(len(arguments[1]) - 5):
        index = 4
        plus_one = 0
        while index > 0:
           summa = arguments[index][i] + five_in_binary_system[index - 1] + plus_one
           plus_one = 0
           if summa >= 2:
               summa -= 2
               plus_one = 1
           rezult[index - 1][i] = summa
           index -= 1
    return rezult


def convert_to_list_constituents(number_form, arguments_number):
    constituents = []
    for number in number_form:
        constituent_list = []
        if arguments_number == 4:
            power = 4 - 1
        else:
            power = 2
        while power >= 0:
            if number >= 2 ** power:
                constituent_list.append(1)
                number -= 2 ** power
            else:
                constituent_list.append(0)
            power -= 1
        constituents.append(constituent_list)
    return constituents


def numeric_form(truth_table, arguments_number):
    rez_num_form = []
    if arguments_number == 4:
        arguments = {"x1": [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                     "x2": [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                     "x3": [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
                     "x4": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]}
    else:
       arguments = {"x1": [0, 0, 0, 0, 1, 1, 1, 1], "x2": [0, 0, 1, 1, 0, 0, 1, 1], "x3": [0, 1, 0, 1, 0, 1, 0, 1]}
    for i in range(len(truth_table)):
       lists = [arguments["x1"][i], arguments["x2"][i], arguments["x3"][i]]
       if arguments_number == 4:
           lists.append(arguments["x4"][i])
       if truth_table[i] == 1:
           rez_num_form.append(index_form(lists))
    return rez_num_form


def index_form(truth_table):
    rez_index = 0
    for i in range(len(truth_table)):
        if truth_table[i] == 1:
            rez_index += 2 ** (len(truth_table) - 1 - i)
    return rez_index


def to_string(formula, arguments_number):
    list_of_brackets = []
    for i in range(len(formula)):
        brackets = []
        if formula[i][0] == 1:
            brackets.append('A')
        elif formula[i][0] == 0:
            brackets.append('(!A)')
        if formula[i][1] == 1:
            brackets.append('B')
        elif formula[i][1] == 0:
            brackets.append('(!B)')
        if formula[i][2] == 1:
            brackets.append('C')
        elif formula[i][2] == 0:
            brackets.append('(!C)')
        if arguments_number == 4:
            if formula[i][3] == 1:
                brackets.append('D')
            elif formula[i][3] == 0:
                brackets.append('(!D)')
        brackets = '&'.join(brackets)
        if len(brackets) > 2:
            brackets = '(' + brackets + ')'
        list_of_brackets.append(brackets)
    return 'v'.join(list_of_brackets)


def total_gluing(formula, number_of_arguments):
    i = number_of_arguments
    while i > 1:
        formula = gluing_formulas(formula, i)
        i -= 1
    return formula

def is_gluable(constituent_1, constituent_2):
    different = 0
    for i in range(len(constituent_1)):
        if constituent_1[i] != constituent_2[i]:
            different += 1
            unnecessary = i
        if different != 1:
            unnecessary = -1  # лишний аргумент
    return unnecessary

def number_of_arguments_in_brackets(brackets):
    number = 0
    for i in range(len(brackets)):
        if brackets[i] != -1:
            number += 1
    return number


def identical_find(implicant, implicants):
   for other in implicants:
       if implicant == other:
           return True
   return False

def gluing_formulas(constituents, arguments_number):
    implicants = []
    first_bracket_index = 0
    i = 0
    for i in range(len(constituents)):
       if number_of_arguments_in_brackets(constituents[i]) == arguments_number:
           first_bracket_index = i
           break
    mas = [False for i in range(len(constituents))]
    for i in range(first_bracket_index, len(constituents)):
       for j in range(i, len(constituents)):
           if is_gluable(constituents[i], constituents[j]) != -1:
              implicant = constituents[i].copy()
              implicant[is_gluable(constituents[i], constituents[j])] = -1
              if not identical_find(implicant, implicants):
                  implicants.append(implicant)
              mas[i] = True
              mas[j] = True
    for i in range(len(mas)):
       if not mas[i]:
           implicants.insert(0, constituents[i])
    return implicants

def args():
    print('\nАргумент 1:')
    plus = plus_5()
    sdnf_A = convert_to_list_constituents(numeric_form(plus[0], 4), 4)
    print('СДНФ:' + to_string(sdnf_A, 4))
    print('ТДНФ:' + to_string(total_gluing(sdnf_A, 4), 4))
    logism = to_string(total_gluing(sdnf_A, 4), 4).replace('!', '~')
    logism = logism.replace('v', '+')
    print('ТДНФ для logism:' + logism)

    print('\nАргумент 2:')
    sdnf_B = convert_to_list_constituents(numeric_form(plus[1], 4), 4)
    print('СДНФ:' + to_string(sdnf_B, 4))
    print('ТДНФ:' + to_string(total_gluing(sdnf_B, 4), 4))
    logism = to_string(total_gluing(sdnf_B, 4), 4).replace('!', '~')
    logism = logism.replace('v', '+')
    print('ТДНФ для logism:' + logism)

    print('\nАргумент 3:')
    sdnf_C = convert_to_list_constituents(numeric_form(plus[2], 4), 4)
    print('СДНФ:' + to_string(sdnf_C, 4))
    print('ТДНФ:' + to_string(total_gluing(sdnf_C, 4), 4))
    logism = to_string(total_gluing(sdnf_C, 4), 4).replace('!', '~')
    logism = logism.replace('v', '+')
    print('ТДНФ для logism:' + logism)

    print('\nАргумент 4:')
    sdnf_D = convert_to_list_constituents(numeric_form(plus[3], 4), 4)
    print('СДНФ:' + to_string(sdnf_D, 4))
    print('ТДНФ:' + to_string(total_gluing(sdnf_D, 4), 4))
    logism = to_string(total_gluing(sdnf_D, 4), 4).replace('!', '~')
    logism = logism.replace('v', '+')
    print('ТДНФ для logism:' + logism)
#
#
