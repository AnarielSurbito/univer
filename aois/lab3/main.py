import formul as sub
# (((A&(!B))v(!A))>C)
function = input(str("Введите формулу\n"))

sub.solution(function)

print("Результат:\n")
sub.get_info()
print('')
print("СДНФ:\n")
sub.SDNF()
print('')
print("СКНФ:\n")
sub.SKNF()
print('')

#Расчётный и  расчётно-табличный метод
print("Расчётный метод для СКНФ")
sub.sKNF()
print('')
print("Расчётный метод для СДНФ")
sub.sDNF()
print('')


#Табличный метод
print("Табличный метод для СКНФ")
sub.tabsknf()
print('')
print("Табличный метод для СДНФ")
sub.tabsdnf()
