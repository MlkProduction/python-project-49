#!/usr/bin/env python3
from brain_games.run_games import run_game
from brain_games.games.even_game import brain_even


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(brain_even, QUESTION)


if __name__ == '__main__':
    main()