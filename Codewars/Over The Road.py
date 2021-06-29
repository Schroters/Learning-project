# Given your house number address and length of street n, give the house number on the opposite side of the street
# Evens increase on the right; odds decrease on the left.
# House numbers start at 1 and increase without gaps.
# When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2
# дается адрес и количество домов на стороне, с обратной стороны они в противоположном направлении считаются

def over_the_road(address, n):
    return n * 2 - address + 1


print(over_the_road(1, 3))      # 6
print(over_the_road(3, 3))      # 4
print(over_the_road(2, 3))      # 5
print(over_the_road(3, 5))      # 8
print(over_the_road(7, 11))     # 16
print(over_the_road(23633656673, 310027696726))     # 596421736780
