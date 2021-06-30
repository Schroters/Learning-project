# The Hashtag Generator
# Here's the deal: It must start with a hashtag (#). All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

def generate_hashtag(line):
    if len(line) == 0 or len(line) > 140:          # Если пусто или больше 140 символов
        return False

    line = line.lower().split()     # в маленький размер и нет пробела
    new_line = '#' + line[0][0].upper() + line[0][1:]   # работа с первым символом и словом

    if len(line) > 1:
        for word in line[1:]:
            new_line += word[0].upper() + word[1:]

    return new_line

def generate_hashtag_2(line):
    if len(line) == 0 or len(line) > 140:          # Если пусто или больше 140 символов
        return False
    output = "#"

    for word in line.split():
        output += word.capitalize()

    return output

print(generate_hashtag(''))
print(generate_hashtag('Do We have A Hashtag'))
print(generate_hashtag('Codewars'))
print(generate_hashtag('Codewars      '))
print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag('codewars is nice'))
print(generate_hashtag('CodeWars is nice'))
print(generate_hashtag('c i n'))
print(generate_hashtag('codewars  is  nice'))
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))

print('\nVer 2 \n')
print(generate_hashtag_2(''))
print(generate_hashtag_2('Do We have A Hashtag'))
print(generate_hashtag_2('Codewars'))
print(generate_hashtag_2('Codewars      '))
print(generate_hashtag_2('Codewars Is Nice'))
print(generate_hashtag_2('codewars is nice'))
print(generate_hashtag_2('CodeWars is nice'))
print(generate_hashtag_2('c i n'))
print(generate_hashtag_2('codewars  is  nice'))
print(generate_hashtag_2('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))
