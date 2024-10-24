import random

def prime_num(num):
    d = 2
    while num % d != 0:
        d += 1
    return d == num

def brain_prime():
        num = random.randint(1, 100)
        if prime_num(num):
            correct_answer = 'yes'

        else:
            correct_answer = 'no'
        return num, correct_answer
