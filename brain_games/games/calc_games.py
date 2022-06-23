from random import randint
from random import choice
MANUAL = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100


def calculate():
    random_number1 = randint(MIN_NUMBER, MAX_NUMBER)
    random_number2 = randint(MIN_NUMBER, MAX_NUMBER)
    random_operator = choice(['*', '+', '-'])
    if random_operator == '*':
        answer = random_number1 * random_number2
    elif random_operator == '+':
        answer = random_number1 + random_number2
    elif random_operator == '-':
        answer = random_number1 - random_number2
    question = (f'{random_number1} {random_operator} {random_number2}')
    return(question, answer, MANUAL)
