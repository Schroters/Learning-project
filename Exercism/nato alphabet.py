# Conversion functions for the NATO Phonetic Alphabet
# https://research.exercism.io/experiment_solutions/413bd25d5b614697bb5a7d7c732b6ccb

import re
# To save a lot of typing the code words are presented here
# as a dict, but feel free to change this if you'd like.
ALPHANUM_TO_NATO = {
    "A": "ALFA",
    "B": "BRAVO",
    "C": "CHARLIE",
    "D": "DELTA",
    "E": "ECHO",
    "F": "FOXTROT",
    "G": "GOLF",
    "H": "HOTEL",
    "I": "INDIA",
    "J": "JULIETT",
    "K": "KILO",
    "L": "LIMA",
    "M": "MIKE",
    "N": "NOVEMBER",
    "O": "OSCAR",
    "P": "PAPA",
    "Q": "QUEBEC",
    "R": "ROMEO",
    "S": "SIERRA",
    "T": "TANGO",
    "U": "UNIFORM",
    "V": "VICTOR",
    "W": "WHISKEY",
    "X": "XRAY",
    "Y": "YANKEE",
    "Z": "ZULU",
    "0": "ZERO",
    "1": "ONE",
    "2": "TWO",
    "3": "TREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINER",
}


def transmit(message: str):  # Convert a message to a NATO code word transmission.
    arr_message, result = re.findall(r'\w', message.upper()), []    # разбили по символам, убрали и подняли
    print(arr_message)
    for i in arr_message:
        if i in ALPHANUM_TO_NATO and i.isascii():
            result.append(ALPHANUM_TO_NATO[i])
    result = ' '.join(result)
    return result


def receive(transmission: str):  # Convert a NATO code word transmission to a message.
    arr_transmission, result = transmission.split(), []
    for i in arr_transmission:
        for alphabet, nato in ALPHANUM_TO_NATO.items():
            if nato == i:
                result.append(alphabet)
    result = ''.join(result)
    return result


print(transmit("Hello, World!")) #"HOTEL ECHO LIMA LIMA OSCAR WHISKEY OSCAR ROMEO LIMA DELTA"
print(transmit("NCC-1701-D"))   #"NOVEMBER CHARLIE CHARLIE ONE SEVEN ZERO ONE DELTA"
print(transmit("hop_lalaley"))
print(receive("HOTEL ECHO LIMA LIMA OSCAR WHISKEY OSCAR ROMEO LIMA DELTA")) #"HELLOWORLD"
print(receive("NOVEMBER CHARLIE CHARLIE ONE SEVEN ZERO ONE DELTA"))         # "NCC1701D"
print(receive("ONE SEVEN ZERO ONE SIERRA TANGO ROMEO INDIA NOVEMBER GOLF WHISKEY HOTEL INDIA TANGO ECHO SIERRA PAPA ALFA CHARLIE ECHO SIERRA TANGO ROMEO INDIA NOVEMBER GOLF PAPA UNIFORM NOVEMBER CHARLIE TANGO UNIFORM ALFA TANGO INDIA OSCAR NOVEMBER"))