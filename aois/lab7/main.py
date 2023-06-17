import func as fun


print('Задание 1')
arr = fun.create_arr(4, 6)
print(arr)

print('\nЗадание 2')
print('0 и 1: ', end='')
fun.compare(0, 0, arr)
print('1 и 0: ', end='')
fun.compare(1, 0, arr)
print('2 и 3: ', end='')
fun.compare(2, 3, arr)

print('\nЗадание 3')
arg = [0, 1, 1, 0, 0, 1]
match, index = fun.search_match(arg, arr)
print('Искомое слово: ', arg, '\nНаибольшее число совпадений: ', match, '\nЭлемент массива: ', arr[index])

print('\nЗадание 4')
print('От минимального к максимальному', fun.sort(arr, 'min'))
print('От максимального к минимальному', fun.sort(arr, 'max'))
