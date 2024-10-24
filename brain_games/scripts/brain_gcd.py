#!/usr/bin/env python3
from brain_games.run_games import run_game
from brain_games.games.gcd_game import brain_gcd


QUESTION = "Find the greatest common divisor of given numbers."


def main():
    run_game(brain_gcd, QUESTION)


if __name__ == '__main__':
    main()
