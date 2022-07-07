from random import randint
MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(random_number):
    if random_number < 2:
        return False
    for i in range(2, random_number):
        if random_number % i == 0:
            return False
    return True


def generate_round_game():
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    question = random_number
    answer = is_prime(random_number) and 'yes' or 'no'
    return(str(question), str(answer))
