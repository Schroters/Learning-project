# Bob
# https://exercism.org/tracks/python/exercises/bob


def response(hey_bob):
    if not hey_bob.strip():
        return "Fine. Be that way!"

    elif hey_bob.strip()[-1] == "?":    # проверяем вопрос ли, дальше регистр
        punctuation = r"""!"#$%&()*+,-./:;<=>@[\]^_`{|}~"""
        for i in hey_bob[:-1]:
            if i.islower() or i.isdigit() or (i in punctuation):
                return "Sure."
        return "Calm down, I know what I'm doing!"

    for i in hey_bob:
        if i.islower():
            return "Whatever."
        elif i.isdigit():
            for j in hey_bob:
                if j.isalpha():
                    return "Whoa, chill out!"
            return "Whatever."
    return "Whoa, chill out!"


print("----------------------------------")
print(response(''))                 # Fine. Be that way!
print(response(' '))                # Fine. Be that way!

print("----------------------------------")
print(response('How are you?'))     # Sure.
print(response("4?"))               # Sure.
print(response(":) ?"))             # Sure.
print(response("Okay if like my  spacebar  quite a bit?   "))  # Sure.

print("----------------------------------")
print(response('YELL AT HIM?'))      # Calm down, I know what I'm doing!
print(response("WHAT'S GOING ON?"))  # Calm down, I know what I'm doing!

print("----------------------------------")
print(response('YELL AT HIM'))      # Whoa, chill out!
print(response("WATCH OUT!"))       # Whoa, chill out!
print(response("1, 2, 3 GO!"))      # Whoa, chill out!
print(response("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"))    # Whoa, chill out!

print("----------------------------------")
print(response('Ha ha ha'))         # Whatever.
print(response("1, 2, 3"))          # Whatever.
