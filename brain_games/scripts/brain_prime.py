from random import randint


def is_prime(number):
    counter = 0
    for i in range(1, number + 1):
        if number % i == 0:
            counter += 1
    return True if counter == 2 or number == 1 else False


def main():
    print("Welcome to the Brain Games")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    correct_answer = 0
    result = 0

    while correct_answer != 3:
        number = randint(1, 11)
        print(f"Question: {number}")

        answer = input("Your answer: ")
        if (answer == "yes" and is_prime(number)) or (
            answer == "no" and not is_prime(number)
        ):
            print("Correct!")
            correct_answer += 1
        else:
            correct_answer = "yes" if is_prime(number) else "no"
            print(
                f"'{answer}' is wrong answer ;(. Correct answer is '{correct_answer}'"
            )
            print(f"Let's try again, {user_name}!")

            break

    if correct_answer == 3:
        print(f"Congratulations, {user_name}!")
    # else:
    # 	print(f"Let's try again, {user_name}!")


if __name__ == "__main__":
    main()
