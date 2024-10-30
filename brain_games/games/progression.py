from random import randint

DISCRIPTION = "What number is missing in the progression?"


def generate_progression():
    progression_length = randint(5, 10)
    initial = randint(1, 100)
    step = randint(1, 10)
    progression = [initial + i * step for i in range(progression_length)]
    hidden_index = randint(0, progression_length - 1)
    return progression, hidden_index


def generate_round():
    progression, hidden_index = generate_progression()
    question = ""
    for i in range(len(progression)):
        if i == hidden_index:
            question += ".. "
        else:
            question += str(progression[i])
            question += " "
    correct_answer = progression[hidden_index]

    return question, str(correct_answer)
