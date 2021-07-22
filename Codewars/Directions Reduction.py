# Directions Reduction
# https://www.codewars.com/kata/550f22f4d758534c1100025a
# Going to one direction and coming back the opposite direction right away is a needless effort.
# Since this is the wild west, with dreadfull weather and not much water,
# it's important to save yourself some energy, otherwise you might die of thirst!


def dirReduc(a):
    starr = " ".join(a)
    starr_repl = starr.replace("NORTH SOUTH", '').replace("SOUTH NORTH", '') \
        .replace("EAST WEST", '').replace("WEST EAST", '')      # замена значений на пустоту
    starr_splt = starr_repl.split()     # новый список
    if len(starr_splt) < len(a):
        # каждый раз возвращает на повтор и если вернул и не поменялось возвращаем значение
        return dirReduc(starr_splt)

    else:
        return starr_splt


print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))     # ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))  # ['WEST']
print(dirReduc(['NORTH']))  # ['NORTH']
print(dirReduc(['NORTH', 'NORTH']))     # ['NORTH', 'NORTH']
print(dirReduc([]))  # []
print(dirReduc(['EAST', 'NORTH']))  # ['EAST', 'NORTH']
print(dirReduc(['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']))
# ['NORTH', 'NORTH']
print(dirReduc(['SOUTH', 'NORTH']))     # []
print(dirReduc(['SOUTH', 'NORTH', 'NORTH']))    # ['NORTH']