# Convert string to camel case
# Function so that it converts dash/underscore delimited words into camel casing. The first word does not change
# Слоа разделенные тире или подчеркиванием превращает в верблюжий регистр, первое слово не меняется
def to_camel_case(text):
    import re

    lt = re.split('[- _]', text)  # список слов разделенных
    nst = lt[0]    # новая будущая строка, первое слово нельзя менять букву

    for i in range(1, len(lt)):
        nst = nst + lt[i][0].upper()+lt[i][1:]  # а тут большой первую букву и добавить остальное

    return nst

print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-stealth-warrior"))
print(to_camel_case(""))
print(to_camel_case("A-B-C"))