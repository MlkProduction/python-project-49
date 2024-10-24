#!/usr/bin/env python3
from brain_games.run_games import run_game
from brain_games.games.prime_game import brain_prime


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_game(brain_prime, QUESTION)


if __name__ == '__main__':
    main()
