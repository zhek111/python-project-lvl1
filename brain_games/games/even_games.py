from random import randint
manual = 'Answer "yes" if the number is even, otherwise answer "no".'


def caclulation():
    random_number = randint(1, 100)
    question = random_number
    answer = random_number % 2 == 0 and 'yes' or 'no'
    return(question, answer)


(question, answer) = caclulation()
