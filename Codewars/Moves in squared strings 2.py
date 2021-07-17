# https://www.codewars.com/kata/56dbe7f113c2f63570000b86
# Moves in squared strings (II)

def rot(s):
    return s[::-1]


def selfie_and_rot(s):
    s = s.split('\n')
    new_list = s.copy()
    dot = '.' * len(s[0])
    for i in range(len(s)):
        new_list.insert(len(s), s[i][::-1])     # на место последнего эллемента в списке добавляем
    new_s = f'{dot}\n'.join(new_list[:len(s)])
    new_s += dot
    for i in new_list[len(s):]:
        new_s += f'\n{dot}' + i

    return new_s


def oper(fct, s):
    return fct(s)


print(oper(rot, "abcd\nefgh\nijkl\nmnop"))          #"ponm\nlkji\nhgfe\ndcba"
print(oper(selfie_and_rot, "abcd\nefgh\nijkl\nmnop"))
# "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"
