import math
import random


def brain_gcd():
    random_number_one = random.randint(0, 10)
    random_number_two = random.randint(0, 10)
    correct_answer = math.gcd(random_number_one, random_number_two)
    random_numbers = f'{random_number_one} {random_number_two}'

    return random_numbers, correct_answer
