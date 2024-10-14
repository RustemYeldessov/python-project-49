from random import randint


def main():
    print("Welcome to the Brain Games")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("Find the greatest common divisor of given numbers.")
    correct_answer = 0
    result = 0

    while correct_answer != 3:

        num1, num2 = randint(1, 100), randint(1, 100)
        # num1 = 77
        # num2 = 81
        print(f"Question: {num1} {num2}")
        for i in range(min(num1, num2), 0, -1):
            if num1 % i == 0 and num2 % i == 0:
                result = i
                break

        answer = int(input("Your answer: "))

        if answer == result:
            print("Correct!")
            correct_answer += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer is {result}")
            print(f"Let's try again, {user_name}!")

            break

        if correct_answer == 3:
            print(f"Congratulations, {user_name}!")

