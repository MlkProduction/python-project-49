import random
import prompt

def main():
    print("Welcome to the Brain Games!")
    brain_prime()

def IsPrime(num):
    d = 2
    while num % d != 0:
        d += 1
    return d == num

def brain_prime():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    right_answer = 0
    correct = 'Correct!'

    while right_answer < 3:
        num = random.randint(1, 100)
        print(f'{'Question:'} {num}')
        answer = input('Your answer: ')

        if answer == 'yes' and IsPrime(num) == True:
            print(correct)
            right_answer += 1

        elif answer == 'no' and IsPrime(num) == False:
            print(correct)
            right_answer += 1

        elif answer == 'yes' and IsPrime(num) == False:
            print(f'{answer} is wrong answer ;(. Correct answer was {'no'}.\nLet\'s try again, {name}')
            break

        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {'yes'}.\nLet\'s try again, {name}')
            break
    if right_answer == 3:
        print(f'{'Congratulations,'} {name}!')

if __name__ == "__main__":
    main()
