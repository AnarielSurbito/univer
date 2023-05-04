import math

def binary(value):
    value = abs(value)
    result = [value % 2]
    while value // 2 > 0:
        value = value // 2
        result.append(value % 2)
    result.reverse()
    return result


def decimal(vec):
    result = 0
    index_coma = len(vec)
    i = 0
    for element in vec:
        if element == -1:
            index_coma = i
            break
        i += 1
    i = index_coma - 1
    j = 0
    while i > -1:
        result += vec[i]*pow(2, j)
        i -= 1
        j += 1
    i = index_coma + 1
    j = -1
    while i < len(vec):
        result += vec[i]*pow(2, j)
        result = round(result, 8)
        i += 1
        j -= 1
    return result


def decimal_diff(vec):
    base = 2
    comma = -1
    result = 0
    index_comma = len(vec)
    i = 0
    while i < len(vec):
        if vec[i] == comma:
            index_comma == i
            break
        i += 1
    i = index_comma - 1
    power = 0
    while i > 0:
        result += vec[i]*pow(base, power)
        i -= 1
        power += 1
    i = index_comma + 1
    j = -1
    while i < len(vec):
        result += vec[i]*pow(base, j)
        i += 1
        j -= 1
    if vec[0] == 1:
        result = result*(-1)
    return result


def binary_dir(value):
    size = 7
    sign = True
    if value > 0:
        sign = False
    result = []
    result = binary(value)
    while len(result) != size:
        result.insert(0, 0)
    if sign:
        result.insert(result[0], 1)
    else:
        result.insert(result[0], 0)
    return result


def binary_rev(value):
    result = list()
    result = binary_dir(value)
    i = 1
    if value < 0:
        while i < len(result):
            if result[i] == 1:
                result[i] = 0
            else:
                result[i] = 1
            i += 1
    return result


def binary_add(value):
    result = list()
    if value < 0:
        result = summ(binary_rev(value), [0, 0, 0, 0, 0, 0, 0, 1])
    else:
        result = binary_dir(value)
    return result


def summ(vec1, vec2):
    size1 = len(vec1)
    size2 = len(vec2)
    if size1 > size2:
        while len(vec1) != len(vec2):
            vec2.insert(vec1[0], 0)
    if size2 > size1:
        while len(vec1) != len(vec2):
            vec1.insert(vec1[0], 0)
    result = list()
    i = 0
    while i < len(vec1):
        result.append(0)
        i += 1
    add_one = True
    i = len(vec1) - 1
    while i >= 0:
        if vec1[i]+vec2[i] == 2:
            if add_one:
                result[i] = 0
            else:
                result[i] = 1
            add_one = False
        elif vec1[i] + vec2[i] == 1:
            if add_one:
                result[i] = 1
            else:
                result[i] = 0
        elif vec1[i] + vec2[i] == 0:
            if add_one:
                result[i] = 0
            else:
                result[i] = 1
                add_one = True
        i -= 1
    return result


def min_part(vec1, vec2):
    result = []
    i = 0
    while i < len(vec1):
        result.append(vec1[i])
        if not is_less(result, vec2):
            return result
        i += 1


def is_less(vec1, vec2):
    x1 = decimal(vec1)
    x2 = decimal(vec2)
    return x1 < x2


def multi(vec1, vec2):
    set = []
    result = []
    size = len(vec2)
    i = size - 1
    j = -1
    while i > -1:
        if vec2[i] == 1:
            dif = size - i - 1
            summand = list()
            for element in vec1:
                summand.append(element)
            while dif:
                summand.append(0)
                dif -= 1
            set.append(summand)



        i -= 1
    result = set[0]
    i = 1
    while i < len(set):
        result = summ(result, set[i])
        i += 1
    return result


def equal_of_orders(vec1, vec2, loob):
    result = []
    zero_numb = 0
    while is_less(vec1, vec2):
        vec1.append(0)
        zero_numb += 1
    result.append(0)
    result.append(-1)
    loob = True
    while zero_numb - 1:
        result.append(0)
        zero_numb -= 1
    return result


def div_int(ind_last_symb, result, part_of_div, vec1, vec2):
    arg1 = list()
    arg2 = list()
    arg1 = binary_add(decimal(part_of_div))
    arg2 = binary_add(decimal(vec2)*(-1))
    part_of_div = summ(arg1, arg2)
    cutting(part_of_div)
    result.append(1)
    while ind_last_symb < len(vec1):
        part_of_div.append(vec1[ind_last_symb])
        cutting(part_of_div)
        if not is_less(part_of_div, vec2):
            arg1 = binary_add(decimal(part_of_div))
            arg2 = binary_add(decimal(vec2)*(-1))
            part_of_div = summ(arg1, arg2)
            result.append(1)
            ind_last_symb += 1
        else:
            result.append(0)
        ind_last_symb += 1
    return ind_last_symb, part_of_div


def cutting(vec):
    if len(vec) >= 8:
        vec.remove(vec[0])
        i = 0
        while i < len(vec):
            if vec[i] == 0:
                vec.remove(vec[0])
            else:
                break


def div_fract(result, part_of_div, vec1, vec2):
    precision = 5
    while precision:
        precision -= 1
        cutting(part_of_div)
        part_of_div.append(0)
        if not is_less(part_of_div, vec2):
            arg1 = binary_add(decimal(part_of_div))
            arg2 = binary_add(decimal(vec2)*(-1))
            part_of_div = summ(arg1, arg2)
            result.append(1)
        else:
            result.append(0)


def div(vec1, vec2):
    result = []
    comma = False
    part_of_div = list()
    if is_less(vec1, vec2):
        result = equal_of_orders(vec1, vec2, comma)
    part_of_div = min_part(vec1, vec2)
    ind_last_symb = len(part_of_div)
    ind_last_symb, part_of_div = div_int(ind_last_symb, result, part_of_div, vec1, vec2)
    if not comma:
        result.append(-1)
    div_fract(result, part_of_div, vec1, vec2)
    return result


def printV(vec):
    i = 0
    while i < len(vec):
        if vec[i] == -1:
            print(",", end='')
        else:
            print(vec[i], end='')
        i += 1
    print(" ")


def menu():
    print("0. +", "1. -", "2. *", "3. /", "4. e")


def norm_float(mantissa, sign, zero_int):
    order = 0
    ind_comma = 0
    float_num = []
    numb = 127
    size_mant = 23
    float_num.append(sign)
    if zero_int:
        i = 0
        while i < len(mantissa):
            if mantissa[i] == 1:
                ind_comma = i
                break
            i = i + 1
        order = (-1)*(ind_comma - 1)
        i = 0
        while i < ind_comma + 1:
            mantissa.remove(mantissa[0])
            i += 1
    else:
        i = 0
        while i < len(mantissa):
            if mantissa[i] == -1:
                ind_comma = i
                break
            i = i + 1
        order = ind_comma - 1
        mantissa.remove(mantissa[0 + ind_comma])
        mantissa.remove(mantissa[0])
    while len(mantissa) < size_mant:
        mantissa.append(0)
    b_order = binary(order + numb)
    add_zero(b_order)
    add_vec(float_num, b_order)
    add_vec(float_num, mantissa)
    return float_num


def add_zero(vec):
    size_order = 8
    if len(vec) < size_order:
        num_zero = size_order - len(vec)
        while num_zero:
            num_zero -= 1
            vec.insert(0, 0)


def add_vec(maing, tail):
    i = 0
    while i < len(tail):
        maing.append(tail[i])
        i += 1


def floating(value):
    sign = 0
    part = 0
    zero_int = False
    if value < 0:
        sign = 1
    value = abs(value)
    fract_part, part = math.modf(value)
    int_part = int(part)
    if part == 0:
        zero_int = True
    rezult_int = []
    result_int = binary(int_part)
    result_int.append(-1)
    result_fract = binary_fract(fract_part)
    i = 0
    while i < len(result_fract):
        result_int.append(result_fract[i])
        i += 1
    result_int = norm_float(result_int, sign, zero_int)
    return result_int


def binary_fract(value):
    result = []
    base = 2
    precision = 30
    power = -1
    try_answer = answer = 0
    while precision:
        precision -= 1
        try_answer += pow(base, power)
        if try_answer <= value:
            result.append(1)
            answer += pow(base, power)
        else:
            result.append(0)
            try_answer = answer
        power -= 1
    return result


def print_float(vec):
    i = 0
    while i < len(vec):
        if i == 1 or i == 9:
            print(" ")
        print(vec[i], end='')
        i = i + 1
    print("\n")


def add_to_dir (vec):
    if vec[0] == 0:
        return vec
    i = 1
    while i < len(vec):
        if vec[i] == 0:
            vec[i] = 1
        elif vec[i] == 1:
            vec[i] = 0
        i += 1
    vec = summ(vec, [0, 0, 0, 0, 0, 0, 0, 1])
    return vec


def float_sum(vec1, vec2):
    size_mant = 23
    order = []
    new_mant = []
    result = [0]
    order1 = []
    order2 = []
    mantissa1 = []
    mantissa2 = []
    order1 = f_get_order(vec1)
    order2 = f_get_order(vec2)
    mantissa1 = f_get_mant(vec1)
    mantissa2 = f_get_mant(vec2)
    ord1 = decimal(order1)
    ord2 = decimal(order2)
    diff = ord1 - ord2
    if not diff == 0:
        if ord1 > ord2:
            order = order1
            new_mant = f_new_mant(abs(diff), mantissa1, mantissa2, order)
        elif ord2 > ord1:
            order = order2
            new_mant = f_new_mant(abs(diff), mantissa2, mantissa1, order)
        i = 0
        while i < len(order):
            result.append(order[i])
            i += 1
        i = 0
        while i < len(new_mant):
            result.append(new_mant[i])
            i += 1
    else:
        mantissa2.insert(0, 0)
        mantissa1.insert(0, 0)
        new_mant = summ(mantissa2, mantissa1)
        if new_mant[0] == 1:
            ord = decimal(order)
            ord += 1
            order = binary(ord)
        else:
            new_mant.remove(new_mant[0])
            while len(new_mant) < size_mant:
                new_mant.append(0)
            i = 0
            while i < len(order):
                result.append(order[i])
                i += 1
            i = 0
            while i < len(new_mant):
                result.append(new_mant[i])
                i += 1
    return result


def f_get_order(vec):
    order = []
    i = 1
    while i < 9:
        order.append(vec[i])
        i += 1
    return order


def f_get_mant(float_numb):
    mantissa = [1]
    i = 9
    while i < 32:
        mantissa.append(float_numb[i])
        i += 1
    return mantissa


def f_new_mant(diff, big, small, order):
    new_mant = [0, 0]
    while diff-1 > 0:
        new_mant.append(0)
        diff -= 1
    i = 0
    while i < len(small) - 1:
        new_mant.append(small[i])
        i += 1
    while len(new_mant) < 25:
        new_mant.append(0)
    while len(new_mant) > 25:
        new_mant.pop()
    big.insert(0, 0)
    new_mantis = summ(new_mant, big)
    if new_mantis[0] == 1:
        ord = decimal(order)
        ord += 1
        order = binary(ord)
    else:
        new_mantis.remove(new_mantis[0])
    new_mantis.remove(new_mantis[0])
    return new_mantis


def float_to_dec(vec):
    number = 127
    rez = 0
    order_v = []
    mantissa = []
    i = 1
    while i < 9:
        order_v.append(vec[i])
        i = i + 1
    order = decimal(order_v) - number
    print(order)
    if order < 0:
        mantissa.append(0)
        mantissa.append(-1)
        while order + 1:
            mantissa.append(0)
            order += 1
        mantissa.append(1)
        i = 9
        while i < 31:
            mantissa.append(vec[i])
            i = i + 1
    elif order > 0:
        mantissa.append(1)
        i = 9
        while i < 31:
            if order == 0:
                mantissa.append(-1)
            mantissa.append(vec[i])
            i += 1
            order -= 1
    elif order == 0:
        mantissa.append(1)
        mantissa.append(-1)
        i = 9
        while i < 31:
            mantissa.append(vec[i])
            i += 1
    rez = decimal(mantissa)
    if vec[0] == 1:
        rez = rez*(-1)
    print(round(rez, 4))


