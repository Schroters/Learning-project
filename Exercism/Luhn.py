# Luhn
# https://exercism.org/tracks/python/exercises/luhn


class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        card_num = self.card_num
        luhn = ""
        card_num = "".join(card_num.split())
        if card_num == "0":
            return False
        for i in range(-1, (len(card_num) + 1) * -1, -1):
            if card_num[i].isdigit():  # проверим цифра ли
                if i % 2 == 0:  # если четное
                    temp_numb = int(card_num[i]) * 2
                    if temp_numb > 9:
                        temp_numb -= 9
                    luhn += str(temp_numb) + " "
                else:
                    luhn += card_num[i] + " "
            else:
                return False
        luhn = sum(list(map(int, luhn.split())))  # проверяем основное условие
        if luhn % 10 == 0:
            return True
        else:
            return False


print(Luhn("4539 3195 0343 6467").valid())  # True
print(Luhn("8273 1232 7352 0569").valid())  # False
print(Luhn("0").valid())                # False
print(Luhn(" 0").valid())               # False
print(Luhn("059").valid())              # True
print(Luhn("055 444 285").valid())      # True
print(Luhn("091").valid())              # True
number = Luhn("055 444 285")
print(number.valid())                   # True
print(number.valid())                   # True
