import random

#EYO function
def EYOrand():

    EYO = ""
    letter = ""

    x = random.randint(1, 99)

    while x != 0:
        if random.randint(0, 10) >= 2:
            letter = "e"
        else:
            letter = "E"
        EYO = EYO + letter
        x = x - 1

    x = random.randint(1, 99)

    while x != 0:
        if random.randint(0, 10) >= 2:
            letter = "y"
        else:
            letter = "Y"
        EYO = EYO + letter
        x = x - 1

    x = random.randint(1, 99)

    while x != 0:
        if random.randint(0, 10) >= 2:
            letter = "o"
        else:
            letter = "O"
        EYO = EYO + letter
        x = x - 1


    return EYO