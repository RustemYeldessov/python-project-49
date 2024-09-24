from random import randint


def main():
    print('Welcome to the Brain Games')
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What number is missing in the progression?')
    correct_answer = 0
    result = 0

    while correct_answer != 3:
        progression = []

        initial = randint(1, 100)
        step = randint(1, 10)

        for i in range(initial, initial + 10 * step, step):
            progression.append(i)

        print('Question: ', end='')
        random_iteration = randint(1, 11)
        for k in range(10):
            if k != random_iteration:
                print(progression[k], end=' ')
            else:
                result = progression[k]
                print('..', end=' ')
        print()
        answer = int(input('Your answer: '))

        if answer == result:
            print('Correct!')
            correct_answer += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer is '{result}'")
            print(f"Let's try again, {user_name}")

            break

    if correct_answer == 3:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}")


if __name__ == '__main__':
    main()
