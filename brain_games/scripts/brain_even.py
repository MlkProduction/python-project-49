#!/usr/bin/env python3
import prompt
import random

def main():
    print("Welcome to the Brain Games!")
    brain_even()
    
def brain_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    right_answer = 0
    correct_answer = 'Correct!'
    while right_answer < 3:
        number = random.randint(0, 100)
        print(f'{'Question:'} {number}')
        answer = input('Your answer: ')
        if number % 2 == 0 and answer == 'yes' or number % 2 != 0 and answer == 'no':
            print(correct_answer)
            right_answer += 1
        elif number % 2 != 0 and answer == 'yes':
            print(f'{"'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again,"} {name}!')
            break
        elif number % 2 == 0 and answer == 'no':
            print(f'{"'no' is wrong answer ;(. Correct answer was 'yes'. Let's try again,"} {name}!')
            break
        else:
            print(f'{name}, {"your answer must be “yes” or “no”! Try again!"}')
            break
    if right_answer == 3:
        print(f'{'Congratulations,'} {name}!')

if __name__ == "__main__":
    main()





