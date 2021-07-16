# https://www.codewars.com/kata/56dbe0e313c2f63be4000b25
# Moves in squared strings (I)

def vert_mirror(s):
    s = s.split('\n')
    new_list = []
    new_s = ''
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


def oper (fct, s):
    return fct(s)


print(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))
# "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw"
print(oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"))
# "yeCt\nCSbg\nJVhv\nlVHt"

