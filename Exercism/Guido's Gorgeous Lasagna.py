# Guido's Gorgeous Lasagna
# https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(minuts):
    """Function that takes the actual minutes the lasagna has been in the oven as an argument
    and returns how many minutes the lasagna still needs to bake"""
    return EXPECTED_BAKE_TIME - minuts


def preparation_time_in_minutes(layers):
    """Function that takes the number of layers you want to add to the lasagna as an argument
    and returns how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare."""
    return layers * 2


def elapsed_time_in_minutes(layers, minuts):
    """Function should return the total number of minutes you've been cooking"""
    return preparation_time_in_minutes(layers) + minuts

print(bake_time_remaining.__doc__)
print(elapsed_time_in_minutes(3, 20))
