from random import randint


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    print("Welcome to the Brain Games")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answers = 0

    while correct_answers != 3:
        number = randint(1, 100)  # Диапазон больше для разнообразия
        print(f"Question: {number}")

        answer = input("Your answer: ").strip().lower()
        correct_answer = "yes" if is_prime(number) else "no"

        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break

    if correct_answers == 3:
        print(f"Congratulations, {user_name}!")
