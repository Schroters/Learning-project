# Sequence Determiner
# https://www.codewars.com/kata/610159919347db0019cabddc
# The 2 main sequences in Mathematics are Arithmetic Progression and Geometric Progression.
# Those are the sequences you will be working with in this kata.


def determine_sequence(series_array):
    rezult = []
    if series_array.count(0) == len(series_array):
        # Тут срабатывает AP
        return 0
    elif series_array.count(series_array[0]) == len(series_array):
        # it is both an AP and GP
        return 2
    elif len(set(series_array)) != len(series_array):   # есть повторы, но меньше чем весь список
        return -1
    distinctionAP = series_array[-1] - series_array[-2]
    distinctionGP = int(series_array[-1] / series_array[-2])
    for i in reversed(range(1, len(series_array))):
        if series_array[i]-distinctionAP != series_array[i-1]:
            rezult.append('AP')
            break
    for i in reversed(range(1, len(series_array))):
        if series_array[i] / series_array[i-1] != distinctionGP:
            rezult.append('GP')
            break
    if len(rezult) == 2:
        return -1
    elif len(rezult) == 0:
        return 2
    elif rezult[0] == 'GP':
        return 0
    elif rezult[0] == "AP":
        return 1


print(determine_sequence([2, 5, 8, 11, 14]))    # 0 Arithmetic Progression
print(determine_sequence([1, 2, 4, 8, 16] ))    # 1 Geometric Progression
print(determine_sequence([1, 2, 1, 3, 4, 5]))   # -1 it doesn't follow any of the above sequences
print(determine_sequence([1, 1, 1, 1, 1]))      # 2  it is both an AP and GP
print(determine_sequence([0, 0, 0, 0, 0]))      # 0 If the series has all 0's, then 0 should be returned as it is not accepted as a term GP
print(determine_sequence([100, 0, 0, 0, 0]))    # -1