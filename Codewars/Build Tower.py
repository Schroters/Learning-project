# Build Tower
# Build Tower by the following given argument:number of floors (integer and always greater than 0).
# Tower block is represented as * . Exampe a tower of 6 floors looks like below:
# '     *     ',1
# '    ***    ',3
# '   *****   ',5
# '  *******  ',7
# ' ********* ',9
# '***********' 11

def tower_builder(n_floors):
    ctr = -1                    # счетчик while
    spn = 1                     # считчик пустот
    tempnumb = ((2 * n_floors) - 1)    # максималка звезд внизу
    b = [''] * n_floors         # пустой список

    b[-1] = tempnumb * '*'      # первая снизу строка
    ctr -= 1                    # minus one indx
    tempnumb -= 2

    while ctr != (n_floors * -1) - 1:
        b[ctr] = (' ' * spn) + (tempnumb) * '*' + (' ' * spn)
        ctr -= 1
        spn += 1
        tempnumb -= 2

    return b

print(tower_builder(3))
print(tower_builder(6))
print(tower_builder(1))
print(tower_builder(100))
