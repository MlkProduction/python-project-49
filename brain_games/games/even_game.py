import random
def brain_even():
        number = random.randint(0, 100) #вынести отдельно
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        return number, correct_answer