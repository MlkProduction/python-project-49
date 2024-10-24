# brain_games/run_games.py

import prompt
from brain_games.scripts.congratulations import congratulations


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_game(game, question):

    name = welcome_user()
    print(question)
    right_answer = 0
    round_game = 3

    while right_answer < round_game:
        question, correct_answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if str(user_answer) == str(correct_answer):
            print('Correct!')
            right_answer += 1
        else:
            print(f"'{user_answer}' is wrong answer ;( "
                  + f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    congratulations(right_answer, round_game, name)
