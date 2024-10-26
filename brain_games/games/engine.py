import prompt

number_of_rounds = 3


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.discription)

    for _ in range(number_of_rounds):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")

    print(f"Congratulations, {name}!")
