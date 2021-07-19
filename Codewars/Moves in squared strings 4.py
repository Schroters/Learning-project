# https://www.codewars.com/kata/56dbf59b0a10feb08c000227
# Moves in squared strings (IV)


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



print('\ndiag_2_sym\n')
print(oper(diag_2_sym, s))      # "plhd\nokgc\nnjfb\nmiea"
print('\nrot_90_counter\n')
print(oper(rot_90_counter, s))  # "dhlp\ncgko\nbfjn\naeim"
print('\nselfie_diag2_counterclock\n')
print(oper(selfie_diag2_counterclock, s))
# "abcd|plhd|dhlp\nefgh|okgc|cgko\nijkl|njfb|bfjn\nmnop|miea|aeim"