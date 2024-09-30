from random import randint


answer = ""


def is_even(number):
    return number % 2 == 0


def main():
    print("Welcome to the Brain Games")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer = 0

    while correct_answer < 3:
        number = randint(1, 100)
        print(f"Question: {number}")
        answer = input(f"Your answer: ").strip().lower()

        # if answer not in ['yes', 'no']:
        #     print("Invalid input. Please answer 'yes' or 'no'.")
        #     continue

        expected_answer = "yes" if is_even(number) else "no"

        if answer == expected_answer:
            print("Correct!")
            correct_answer += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{expected_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
