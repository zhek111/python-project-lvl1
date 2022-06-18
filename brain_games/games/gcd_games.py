from random import randint
from math import gcd
manual = 'Find the greatest common divisor of given numbers.'


def caclulation():
    start_number = 1
    end_number = 100
    random_number1 = randint(start_number, end_number)
    random_number2 = randint(start_number, end_number)
    example1 = (f'{random_number1} {random_number2}')
    answer1 = gcd(random_number1, random_number2)
    list = [example1, answer1]
    question = list[0]
    answer = list[1]
    return(question, answer)
