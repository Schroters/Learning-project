# Strings: swap vowels' case
# https://www.codewars.com/kata/5803c0c6ab6c20a06f000026
# Given a string, return a copy of the string with the vowels' case swapped.
# Для данной строки вернуть копию строки с замененным регистром гласных.
def swap_vowel_case(st):
    vowels, new_st = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"], ""
    for i in st:
        if i in vowels:
            if i.islower():
                new_st += i.upper()
            elif i.isupper():
                new_st += i.lower()
        else:
            new_st += i
    return new_st


print(swap_vowel_case("C Is AlIvE!"))    # C is alive!
print(swap_vowel_case("to"))    # tO
print(swap_vowel_case("simply"))    # sImply
