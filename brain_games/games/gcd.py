from random import randint

DISCRIPTION = "Find the greatest common divisor of given numbers."


def generate_round():
    num1, num2 = randint(1, 100), randint(1, 100)
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            correct_answer = i
            break
    question = str(num1) + " " + str(num2)
    return question, str(correct_answer)
