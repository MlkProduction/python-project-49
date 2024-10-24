#!/usr/bin/env python3
from brain_games.run_games import run_game
from brain_games.games.calc_game import brain_calc


QUESTION = 'What is the result of the expression?'


def main():
    run_game(brain_calc, QUESTION)


if __name__ == '__main__':
    main()
