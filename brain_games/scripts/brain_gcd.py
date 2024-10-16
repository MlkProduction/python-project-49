from random import randint

import math
import prompt
import random

def main():
    print("Welcome to the Brain Games!")
    brain_gcd()


def brain_gcd():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What is the result of the expression?")
    right_answer = 0
    correct = 'Correct!'
    while right_answer < 3:
        random_number_one = randint(0, 10)
        random_number_two = randint(0, 10)
        correct_answer = math.gcd(random_number_one, random_number_two)
        print(f'{'Question:'} {random_number_one} {random_number_two}')

        answer = input('Your answer: ')

        if int(answer) == math.gcd(random_number_one, random_number_two):
            print(correct)
            right_answer += 1

        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer} ')
            break

    if right_answer == 3:
        print(f'{'Congratulations,'} {name}!')


if __name__ == "__main__":
    main()

