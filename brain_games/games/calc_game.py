import random

def brain_calc():
    random_number_one = random.randint(0, 10)
    random_number_two = random.randint(0, 10)
    operator = ['+', '-', '*']
    random_operator = random.choice(operator)
    task = f'{random_number_one} {random_operator} {random_number_two}'

    correct_answer = 0
    if random_operator == operator[0]:
        correct_answer = random_number_one + random_number_two

    elif random_operator == operator[1]:
        correct_answer = random_number_one - random_number_two

    elif random_operator == operator[2]:
        correct_answer = random_number_one * random_number_two
    return task, correct_answer

