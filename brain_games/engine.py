import prompt
from brain_games.cli import welcome_user

NUMBER_OF_ROUNDS = 3


def run_game(game):
    user_name = welcome_user()
    print(game.DISCRIPTION)

    for _ in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        print("Correct!")

    print(f"Congratulations, {user_name}!")
