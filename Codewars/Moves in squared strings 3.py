# https://www.codewars.com/kata/56dbeec613c2f63be4000be6
# Moves in squared strings (III)

def rot_90_clock(s):
    s = s.split('\n')
    new_list = []
    time_line = ''
    for i in range(len(s)):
        for j in reversed(range(len(s))):
            time_line += s[j][i]
        new_list.append(time_line)
        time_line = ''
    new_s = '\n'.join(new_list)
    return new_s


def diag_1_sym(s):
    s = s.split('\n')
    new_list = []
    time_line = ''
    for i in range(len(s)):
        for j in range(len(s)):
            time_line += s[j][i]
        new_list.append(time_line)
        time_line = ''
    new_s = '\n'.join(new_list)
    return new_s

def selfie_and_diag1(s):
    s = s.split('\n')
    new_list = []
    time_line = ''
    for i in range(len(s)):
        for j in range(len(s)):
            time_line += s[j][i]
        time_line = s[i] + '|' + time_line
        new_list.append(time_line)
        time_line = ''
    new_s = '\n'.join(new_list)
    return new_s


def oper(fct, s):
    return fct(s)


s = 'abcd\nefgh\nijkl\nmnop'
print('\ndiag_1_sym\n')
print(oper(diag_1_sym, s))    # aeim\nbfjn\ncgko\ndhlp
print('\nrot_90_clock\n')
print(oper(rot_90_clock, s))  # miea\nnjfb\nokgc\nplhd
print('\nselfie_and_diag1\n')
print(oper(selfie_and_diag1, s)) #"abcd|aeim\nefgh|bfjn\nijkl|cgko\nmnop|dhlp"
print('\n\n')