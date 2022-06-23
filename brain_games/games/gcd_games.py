from random import randint
from math import gcd
MANUAL = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def calculate():
    random_number1 = randint(MIN_NUMBER, MAX_NUMBER)
    random_number2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = (f'{random_number1} {random_number2}')
    answer = gcd(random_number1, random_number2)
    return(question, answer, MANUAL)
