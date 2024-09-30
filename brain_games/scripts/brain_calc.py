from random import randint, choice

def main():
    operations = ['+', '-', '/', '*']
    print('Welcome to the Brain Games')
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What is the result of the expression? ')
    correct_answer = 0
    result = 0
    while correct_answer < 3:
        num1, num2 = randint(1, 9), randint(1, 9)
        random_operation = choice(operations)
        if random_operation == '+':
            print(f'Question: {num1} + {num2}')
            result = num1 + num2
        elif random_operation == '-':
            print(f'Question: {num1} - {num2}')
            result = num1 - num2
        elif random_operation == '*':
            print(f'Question: {num1} * {num2}')
            result = num1 * num2
        elif random_operation == '/' and num1 % num2 == 0:
            print(f'Question: {num1} / {num2}')
            result = num1 / num2
        else:
            continue

        answer = int(input('Your answer: '))

        if answer == result:
            print('Correct!')
            correct_answer += 1
        else:
            print(f'{answer} is wrong answer ;(. Correct answer is {result}')
            print(f"Let's try again, {user_name}!")

            break

        if correct_answer == 3:
            print(f'Congratulations, {user_name}!')
        # else:
        #     print(f"Let's try again, {user_name}")

if __name__ == '__main__':
    main()