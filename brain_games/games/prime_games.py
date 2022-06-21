from random import randint
from brain_games.games.logic_games import tune
MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def calculate():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)

    def make_list_prime(MAX_NUMBER):
        list = []
        for i in range(2, MAX_NUMBER):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                list.append(i)
        return list
    list = make_list_prime(MAX_NUMBER)
    question = random_number
    answer = random_number in list and 'yes' or 'no'
    return(question, answer, MANUAL)


print(tune(calculate))
