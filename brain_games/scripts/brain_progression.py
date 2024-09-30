from random import randint


def main():
    print('Welcome to the Brain Games')
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What number is missing in the progression?')
    correct_answer = 0

    while correct_answer != 3:
        progression = []

        progression_length = randint(5, 10)
        initial = randint(1, 100)
        step = randint(1, 10)

        for i in range(progression_length):
            progression.append(initial + i * step)

        hidden_index = randint(0, progression_length - 1)
        hidden_value = progression[hidden_index]

        print('Question:', end=' ')
        for i in range(progression_length):
            if i == hidden_index:
                print('..', end=' ')
            else:
                print(progression[i], end=' ')
        print()

        answer = input('Your answer: ')

        if answer.isdigit() and int(answer) == hidden_value:
            print('Correct!')
            correct_answer += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{hidden_value}'.")
            print(f"Let's try again, {user_name}!")
            break

    if correct_answer == 3:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}!")


if __name__ == '__main__':
    main()
