from random import randint, choice

discription = "What is the result of the expression? "

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2

def generate_round():
    num1, num2 = randint(1, 9), randint(1, 9)
    operations = ["+", "-", "*"]
    operation = choice(operations)
    correct_answer = calculate(num1, num2, operation)
    question = str(num1) + ' ' + str(operation) + ' ' + str(num2)
    return question, str(correct_answer)


    #     answer = input("Your answer: ")
    #     if answer == str(result):
    #         correct_answers += 1
    #         print("Correct!")
    #     else:
    #         print(f"{answer} is wrong answer ;(. Correct answer is {result}")
    #         print(f"Let's try again, {user_name}!")
    #         break
    #
    # if correct_answers == 3:
    #     print(f"Congratulations, {user_name}!")
