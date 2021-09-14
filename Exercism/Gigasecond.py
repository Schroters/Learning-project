# Gigasecond
# https://exercism.org/tracks/python/exercises/gigasecond
# Given a moment, determine the moment that would be after a gigasecond has passed.
# A gigasecond is 10^9 (1,000,000,000) seconds.
from datetime import datetime


def add(moment):
    Gigasecond = 1000000000
    moment = moment.timestamp() + Gigasecond
    return datetime.fromtimestamp(moment)


print(add(datetime(2011, 4, 25, 0, 0)))
