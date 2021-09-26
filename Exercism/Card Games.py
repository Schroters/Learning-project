# Card Games
# https://exercism.org/tracks/python/exercises/card-games


def get_rounds(number):
    return [number, number+1, number+2]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    return (sum(hand) / len(hand)) == ((hand[0] + hand[-1]) / 2)


def average_even_is_average_odd(hand):
    return (sum(hand[::2]) / len(hand[::2])) == (sum(hand[1::2]) / len(hand[1::2]))


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = 22
    return hand


print(get_rounds(27))
print(concatenate_rounds([27, 28, 29], [35, 36]))
print(list_contains_round([27, 28, 29, 35, 36], 29))
print(list_contains_round([27, 28, 29, 35, 36], 30))
print(card_average([5, 6, 7]))
print(approx_average_is_average([1, 2, 3]))
print(approx_average_is_average([2, 3, 4, 8, 8]))
print(approx_average_is_average([1, 2, 3, 5, 9]))
print(average_even_is_average_odd([1, 2, 3]))
print(average_even_is_average_odd([1, 2, 3, 4]))

hand = [5, 9, 11]
maybe_double_last(hand)
print(hand)     # [5, 9, 22]

hand = [5, 9, 10]
maybe_double_last(hand)
print(hand)     # [5, 9, 10]
