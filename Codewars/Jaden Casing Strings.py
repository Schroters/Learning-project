# Jaden Casing Strings
# Каждое слово в строке должно начинаться с большой буквы
# Have to capitalize each word
def to_jaden_case(string):
    ms = string.split()
    nms = []
    for i in ms:
        ni = i[0].upper() + i[1:]
        nms += [ni]
    str = ' '.join(nms)
    return str

quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))