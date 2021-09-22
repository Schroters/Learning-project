# Little Sister's Vocabulary
# https://exercism.org/tracks/python/exercises/little-sisters-vocab


def add_prefix_un(word): return 'un' + word


def make_word_groups(vocab_words):
    answer = vocab_words[0]
    for i in vocab_words[1:]:
        answer = answer + ' :: ' + vocab_words[0] + i
    return answer


def remove_suffix_ness(word):
    new_word = word.split('ness')[0]
    if new_word[-1] == "i":
        return new_word[:-1] + 'y'
    else:
        return new_word


def noun_to_verb(sentence, index):
    sentence = sentence.split()
    return ''.join(filter(str.isalpha, sentence[index])) + 'en'


print(add_prefix_un('happy'))
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
print(remove_suffix_ness("heaviness"))
print(remove_suffix_ness("sadness"))
print(noun_to_verb('I need to make that bright.', -1))
print(noun_to_verb('It got dark as the sun set.', 2))
