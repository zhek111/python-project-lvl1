from brain_games.games.is_prime import is_prime
from random import randint
manual = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def caclulation():
    start_number = 1
    end_number = 100
    random_number = randint(start_number, end_number)
    list = is_prime(end_number)
    question = random_number
    answer = random_number in list and 'yes' or 'no'
    return(question, answer)
