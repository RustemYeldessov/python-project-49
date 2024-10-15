from random import randint, choice


def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2


def main():
    print("Welcome to the Brain Games")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("What is the result of the expression? ")

    correct_answers = 0
    while correct_answers < 3:
        num1, num2 = randint(1, 9), randint(1, 9)
        operations = ["+", "-", "*"]
        operation = choice(operations)
        result = calculate(num1, num2, operation)
        print(f"Question: {num1} {operation} {num2}")

        answer = input("Your answer: ")
        if answer == str(result):
            correct_answers += 1
            print("Correct!")
        else:
            print(f"{answer} is wrong answer ;(. Correct answer is {result}")
            print(f"Let's try again, {user_name}!")
            break

    if correct_answers == 3:
        print(f"Congratulations, {user_name}!")
