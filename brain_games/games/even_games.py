from random import randint
manual = 'Answer "yes" if the number is even, otherwise answer "no".'


def caclulation():
    start_number = 1
    end_number = 100
    random_number = randint(start_number, end_number)
    question = random_number
    answer = random_number % 2 == 0 and 'yes' or 'no'
    return(question, answer)
