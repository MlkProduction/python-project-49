import random
import prompt

def main():
    print("Welcome to the Brain Games!")
    brain_progression()

def arifmetic_progression(start, step, n):
    progression = []
    for i in range(n):
        progression.append(start + i * step)
    return progression


def brain_progression():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What number is missing in the progression?")
    right_answer = 0
    correct = 'Correct!'

    while right_answer < 3:

        start = random.randint(1, 10)
        step = random.randint(1, 10)
        n = 5
        progression = arifmetic_progression(start, step, n)
        hidden_index = random.randint(0, n - 1)
        hidden_number = progression[hidden_index]
        progression[hidden_index] = '..'

        print('Question:', end = ' ')
        for num in progression:
            print(num, end = ' ')
        print()
        answer = input('Your answer: ')

        if int(answer) == hidden_number:
            print(correct)
            right_answer += 1

        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {hidden_number}.\nLet\'s try again, {name}')

            break

    if right_answer == 3:
        print(f'{'Congratulations,'} {name}!')

if __name__ == "__main__":
    main()
