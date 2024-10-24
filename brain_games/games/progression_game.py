import random

def arifmetic_progression(start, step, n):
    progression = []
    for i in range(n):
        progression.append(start + i * step)
    return progression


def brain_progression():

        start = random.randint(1, 10)
        step = random.randint(1, 10)
        n = 5
        progression = arifmetic_progression(start, step, n)
        hidden_index = random.randint(0, n - 1)
        hidden_number = progression[hidden_index]
        progression[hidden_index] = '..'
        progression = ' '.join(str(num) for num in progression)
        correct_answer = hidden_number
        return correct_answer, progression