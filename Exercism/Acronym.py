# Acronym
# https://exercism.org/tracks/python/exercises/acronym


def abbreviate(words):
    rez = ""
    words = words.replace("-", " ").replace("_", " ").split()
    for i in words:
        rez += i[0].upper()
    return rez


print(abbreviate("Three Letter Acronyms"))                      # TLA
print(abbreviate("Portable Network Graphics"))                  # PNG
print(abbreviate("GNU Image Manipulation Program"))             # GIMP
print(abbreviate("Complementary metal-oxide semiconductor"))    # CMOS
print(abbreviate("Something - I made up from thin air"))        # SIMUFTA
print(abbreviate("The Road _Not_ Taken"))                       # TRNT
