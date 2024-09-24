from random import randint


answer = ''

def is_even(number):
    return number % 2 == 0

def main():
    print('Welcome to the Brain Games')
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer = 0
    while correct_answer != 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = input(f'Your answer: ')

        if (answer == 'yes' and is_even(number)) or (answer == 'no' and not is_even(number)):
            print('Correct!')
            correct_answer += 1
        else:
            correct_answer = 'yes' if is_even(number) else 'no'
            print(f"'{answer}' is wrong answer ;(. Correct answer is '{correct_answer}'")
            break

    if correct_answer == 3:
        print(f'Congratulations, {user_name}!')
    else:
        print(f"Let's try again, {user_name}")


if __name__ == '__main__':
    main()

