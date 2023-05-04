import func


key = 10
x1 = int(input("Введите х1\n"))
x2 = int(input("Введите х2\n"))
sings = [0, 0]
if x1 < 0:
    sings[0] = 1
if x2 < 0:
    sings[1] = 1
arg1 = func.binary_add(x1)
arg2 = func.binary_add(x2)
arg1_min = func.binary_add(x2*(-1))
arg2_min = func.binary_add(x1*(-1))
arg1_b = func.binary(x1)
arg2_b = func.binary(x2)
func.menu()
while key > (-1):
    key = int(input())
    if key == 0:
        temp = func.summ(arg1, arg2)
        rezult = func.add_to_dir(temp)
        func.printV(rezult)
        print(func.decimal_diff(rezult))

    if key == 1:
        temp = func.summ(arg1, arg1_min)
        func.printV(func.add_to_dir(temp))
        print(func.decimal_diff(func.add_to_dir(temp)))

    if key == 2:
        temp = func.multi(func.binary_dir(abs(x1)), func.binary_dir(abs(x2)))
        func.printV(temp)
        if sings[0] + sings[1] == 1:
            print("-")
        else:
            print("+")
        print(func.decimal(temp))

    if key == 3:
        if sings[0] + sings[1] == 1:
            print("-")
        else:
            print("+")
        temp = func.div(arg1_b, arg2_b)
        func.printV(temp)
        print(func.decimal(temp))

    if key == 4:
        x = float(input())
        y = float(input())
        temp1 = func.floating(x)
        func.print_float(temp1)
        func.float_to_dec(temp1)
        temp2 = func.floating(y)
        func.print_float(temp2)
        func.float_to_dec(temp2)
        temp = func.float_sum(temp1, temp2)
        func.print_float(temp)
        func.float_to_dec(temp)

