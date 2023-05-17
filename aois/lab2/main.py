import subformul as sub
# (((A&(!B))v(!A))>C)
# ((((P>R)&(Q>S))&((!P)v(!S)))>((!P)v(!Q)))
function = input(str("Введите формулу\n"))

sub.solution(function)
sub.get_info()
print("")
print("СДНФ:\n")
sub.SDNF()
print("")
print("СКНФ:\n")
sub.SKNF()
