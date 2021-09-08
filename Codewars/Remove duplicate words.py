# Remove duplicate words
# https://www.codewars.com/kata/5b39e3772ae7545f650000fc
# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.


def delete_duplicate_words_ithout_saving_the_position(s):
    return " ".join(list(set(s.split())))


def remove_duplicate_words(s):
    result = []
    for i in s.split():
        if i not in result:
            result.append(i)
    return " ".join(result)


print(delete_duplicate_words_ithout_saving_the_position('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))
print(remove_duplicate_words('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))
s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
result = ' '.join(dict.fromkeys(s.split()))     # another way
print(result)