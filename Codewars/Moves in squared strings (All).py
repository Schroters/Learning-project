# https://www.codewars.com/kata/56dbe0e313c2f63be4000b25
# Moves in squared strings (I)
# https://www.codewars.com/kata/56dbe7f113c2f63570000b86
# Moves in squared strings (II)
# https://www.codewars.com/kata/56dbeec613c2f63be4000be6
# Moves in squared strings (III)
# https://www.codewars.com/kata/56dbf59b0a10feb08c000227
# Moves in squared strings (IV)


def vert_mirror(s):
    s = s.split('\n')
    new_list = []
    for i in range(len(s)):
        new_list += [s[i][::-1]]
    new_s = '\n'.join(new_list)
    return new_s


def hor_mirror(s):
    s = s.split('\n')
    new_list = []
    for i in s:
        new_list.insert(0, i)
    new_s = '\n'.join(new_list)
    return new_s


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


def rot_90_clock(s):
    s = s.split('\n')
    new_list, time_line = [], ''
    for i in range(len(s)):
        for j in reversed(range(len(s))):
            time_line += s[j][i]
        new_list.append(time_line)
        time_line = ''
    new_s = '\n'.join(new_list)
    return new_s


def diag_1_sym(s):
    s = s.split('\n')
    new_list, time_line = [], ''
    for i in range(len(s)):
        for j in range(len(s)):
            time_line += s[j][i]
        new_list.append(time_line)
        time_line = ''
    new_s = '\n'.join(new_list)
    return new_s


def selfie_and_diag1(s):
    s = s.split('\n')
    new_list, time_line = [], ''
    for i in range(len(s)):
        for j in range(len(s)):
            time_line += s[j][i]
        time_line = s[i] + '|' + time_line
        new_list.append(time_line)
        time_line = ''
    new_s = '\n'.join(new_list)
    return new_s


def diag_2_sym(s):
    s = s.split('\n')
    new_list, time_line = [], ''
    for i in reversed(range(len(s))):
        for j in reversed(range(len(s))):
            time_line += s[j][i]
        new_list.append(time_line)
        time_line = ''
    new_s = '\n'.join(new_list)
    return new_s


def rot_90_counter(s):
    s = s.split('\n')
    new_list, time_line = [], ''
    for i in reversed(range(len(s))):
        for j in range(len(s)):
            time_line += s[j][i]
        new_list.append(time_line)
        time_line = ''
    new_s = '\n'.join(new_list)
    return new_s


def selfie_diag2_counterclock(s):
    s1, s2, s3 = s.split(), diag_2_sym(s).split(), rot_90_counter(s).split()
    for i in range(len(s1)):
        s1[i] = s1[i] + '|' + s2[i] + '|' + s3[i]
    new_s = '\n'.join(s1)
    return new_s


def oper(fct, s):
    return fct(s)


s = 'abcd\nefgh\nijkl\nmnop'
print('\nTest data \nvert_mirror\n')
print(oper(vert_mirror, s))  #"dcba\nhgfe\nlkji\nponm"
print('\nhor_mirror\n')
print(oper(hor_mirror, s))   #"mnop\nijkl\nefgh\nabcd"
print('\nrot\n')
print(oper(rot, s))          #"ponm\nlkji\nhgfe\ndcba"
print('\nselfie_and_rot\n')
print(oper(selfie_and_rot, s))  # "abcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba"
print('\ndiag_1_sym\n')
print(oper(diag_1_sym, s))    # aeim\nbfjn\ncgko\ndhlp
print('\nrot_90_clock\n')
print(oper(rot_90_clock, s))  # miea\nnjfb\nokgc\nplhd
print('\nselfie_and_diag1\n')
print(oper(selfie_and_diag1, s)) #"abcd|aeim\nefgh|bfjn\nijkl|cgko\nmnop|dhlp"
print('\ndiag_2_sym\n')
print(oper(diag_2_sym, s))      # "plhd\nokgc\nnjfb\nmiea"
print('\nrot_90_counter\n')
print(oper(rot_90_counter, s))  # "dhlp\ncgko\nbfjn\naeim"
print('\nselfie_diag2_counterclock\n')
print(oper(selfie_diag2_counterclock, s))
# "abcd|plhd|dhlp\nefgh|okgc|cgko\nijkl|njfb|bfjn\nmnop|miea|aeim"

