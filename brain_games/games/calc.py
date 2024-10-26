from random import randint, choice

discription = "What is the result of the expression? "


def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2


def generate_round():
    num1, num2 = randint(1, 9), randint(1, 9)
    operations = ["+", "-", "*"]
    operation = choice(operations)
    correct_answer = calculate(num1, num2, operation)
    question = str(num1) + " " + str(operation) + " " + str(num2)
    return question, str(correct_answer)
