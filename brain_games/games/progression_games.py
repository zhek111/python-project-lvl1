from random import randint
from brain_games.games.logic_games import tune
MANUAL = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_STEP = 1
MAX_STEP = 12
MIN_NUMBER_STEPS = 5
MAX_NUMBER_STEPS = 10
FIRST_ELEMENT_PROGRESSION = 0


def caclulate():
    start_progression = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_STEP, MAX_STEP)
    number_steps = randint(MIN_NUMBER_STEPS, MAX_NUMBER_STEPS)
    end_progression = start_progression + step * number_steps
    progression = (list(range(start_progression, end_progression, step)))
    random_number = (randint(FIRST_ELEMENT_PROGRESSION, number_steps - 1))
    answer = progression[random_number]
    progression[random_number] = '..'

    def corr_str():
        question = ''
        for number in progression:
            question = question + str(number) + " "
        return question
    question = corr_str()
    question = question.strip()
    return(question, answer, MANUAL)


print(tune(caclulate))
