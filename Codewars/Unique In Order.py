#Unique In Order
# Implement the function which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of elements.

def unique_in_order(iterable):
    newli = []
    if len(iterable) > 0:                   # проверка на пустой список check empty list
        for i in range(len(iterable) - 1):
            if iterable[i] != iterable[i+1]:
                newli += [iterable[i]]

        newli += [iterable[-1]]
    return newli


print(unique_in_order('AAAABBBCCDAABBB')) #== ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD'))         #== ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_in_order([1,2,2,3,3]))       #== [1,2,3]
print(unique_in_order([]))