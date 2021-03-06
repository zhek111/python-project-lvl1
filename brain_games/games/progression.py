from random import randint
MANUAL = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
MIN_STEP = 1
MAX_STEP = 12
MIN_COUNT_STEPS = 5
MAX_COUNT_STEPS = 10
FIRST_ELEMENT_PROGRESSION = 0


def generate_round_game():
    start_progression = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_STEP, MAX_STEP)
    number_count = randint(MIN_COUNT_STEPS, MAX_COUNT_STEPS)
    end_progression = start_progression + step * number_count
    progression = (list(range(start_progression, end_progression, step)))
    random_number = (randint(FIRST_ELEMENT_PROGRESSION, number_count - 1))
    answer = progression[random_number]
    progression[random_number] = '..'
    question = ''
    for number in progression:
        question = question + str(number) + " "
    question = question.strip()
    return(str(question), str(answer))
