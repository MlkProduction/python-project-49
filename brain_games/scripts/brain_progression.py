#!/usr/bin/env python3
from brain_games.run_games import run_game
from brain_games.games.progression_game import brain_progression


QUESTION = "What number is missing in the progression?"


def main():
    run_game(brain_progression, QUESTION)


if __name__ == '__main__':
    main()