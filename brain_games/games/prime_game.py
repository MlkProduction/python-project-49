import random

def IsPrime(num):
    d = 2
    while num % d != 0:
        d += 1
    return d == num
correct_answer = ' '
def brain_prime():
        num = random.randint(1, 100)
        if  IsPrime(num) == True:
            correct_answer == 'yes'

        elif  IsPrime(num) == False:
            correct_answer == 'no'

