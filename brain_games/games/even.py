from random import randint

discription = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    number = randint(1, 100)
    correct_answer = "yes" if number % 2 == 0 else "no"
    return number, correct_answer
