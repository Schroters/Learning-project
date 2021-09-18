# Currency Exchange
# https://exercism.org/tracks/python/exercises/currency-exchange
def estimate_value(budget, exchange_rate): return budget / exchange_rate


def get_change(budget, exchanging_value): return budget - exchanging_value


def get_value(denomination, number_of_bills): return denomination * number_of_bills


def get_number_of_bills(budget, denomination): return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    return int(denomination * (budget / (exchange_rate + exchange_rate / 100 * spread) // denomination))


def unexchangeable_value(budget, exchange_rate, spread, denomination):
    return int((budget // (exchange_rate * (1 + spread / 100)))) - exchangeable_value(budget, exchange_rate, spread, denomination)


print(estimate_value(127.5, 1.2))   # 106.25
print(get_change(127.5, 120))       # 7.5
print(get_value(5, 128))            # 640
print(get_number_of_bills(127.5, 5))    # 25
print(exchangeable_value(127.25, 1.20, 10, 20))     # 80
print(exchangeable_value(127.25, 1.20, 10, 5))      # 95
print(unexchangeable_value(127.25, 1.20, 10, 20))   # 16
print(unexchangeable_value(127.25, 1.20, 10, 5))    # 1
