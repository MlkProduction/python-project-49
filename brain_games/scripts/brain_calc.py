from random import randint

import prompt
import random

def main():
    print("Welcome to the Brain Games!")
    brain_calc()

def brain_calc():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What is the result of the expression?")
    right_answer = 0
    correct = 'Correct!'
    while right_answer < 3:
        random_number_one = randint(0, 10)
        random_number_two = randint(0, 10)
        operator = ['+', '-', '*']
        random_operator = random.choice(operator)
        task = f'{random_number_one} {random_operator} {random_number_two}'
        correct_answer = 0

        if random_operator == operator[0]:
            correct_answer = random_number_one + random_number_two

        elif random_operator ==  operator[1]:
            correct_answer = random_number_one - random_number_two

        elif random_operator ==  operator[2]:
            correct_answer  = random_number_one * random_number_two

        print(f'{'Question:'} {task}')
        answer = input('Your answer: ')

        if int(answer) == correct_answer:
            print(correct)
            right_answer += 1

        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer} ')
            break
    if right_answer == 3:
        print(f'{'Congratulations,'} {name}!')



if __name__ == "__main__":
    main()

