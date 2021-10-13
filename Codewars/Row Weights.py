# Row Weights
# https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9

def row_weights(array):
    return sum(array[::2]), sum(array[1::2])


print(row_weights([80]))
print(row_weights([100, 50]))
print(row_weights([0]))
