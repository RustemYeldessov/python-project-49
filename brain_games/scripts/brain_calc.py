from random import randint, choice


def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2


def ask_question():
    num1, num2 = randint(1, 9), randint(1, 9)
    operations = ["+", "-", "*"]
    operation = choice(operations)
    result = calculate(num1, num2, operation)
    print(f"Question: {num1} {operation} {num2}")
    return result


def main():
    print("Welcome to the Brain Games")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("What is the result of the expression? ")

    correct_answer = 0
    while correct_answer < 3:
        result = ask_question()
        try:
            answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if answer == result:
            print("Correct!")
            correct_answer += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer is {result}")
            print(f"Let's try again, {user_name}!")
            break

    if correct_answer == 3:
        print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
