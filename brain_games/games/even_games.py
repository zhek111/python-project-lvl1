from random import randint
MANUAL = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def calculate():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    question = random_number
    answer = random_number % 2 == 0 and 'yes' or 'no'
    return(question, answer, MANUAL)
