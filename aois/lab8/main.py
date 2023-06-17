import func


print('Горизонтальная таблица')
arr = func.tab_hor()
func.print_list(arr)

print('\nДиагональная таблица(слова расположены вертикально со смещением)')
func.print_list(func.change_vert(arr))

print('\nЧтение с диагональной по 1 индексу')
print(func.read_vert(1, func.change_vert(arr)))

print('\nЧтение с диагональной по 5 индексу')
print(func.read_vert(5, func.change_vert(arr)))


print('\nПоиск по индексу')
func.search(0, arr)
func.search(15, arr)

print('\nУстановка значения по индексу')
func.setter(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], arr)
func.print_list(arr)

print('\nЛогические операции над словами(указаны по индексу), перезапись в индекс для второго слова (второго аргумента)')
print('1-2,f4')
func.log_oper(1, 2, 'f4', arr)
func.print_list(arr)
print('\n1-3,f6')
func.log_oper(1, 3, 'f6', arr)
func.print_list(arr)
print('\n1-4,f9')
func.log_oper(1, 4, 'f9', arr)
func.print_list(arr)
print('\n1-5,f11')
func.log_oper(1, 5, 'f11', arr)
func.print_list(arr)

print('\nСортировка')
func.print_list(func.sort(arr, 'max'))


print('\nСумма по ключу')
func.summ([1, 0, 1], arr)
func.print_list(arr)
