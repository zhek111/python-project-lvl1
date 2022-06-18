from random import randint
manual = 'What number is missing in the progression?'


def caclulation():
    start_number = 1
    end_number = 100
    start_progression = randint(start_number, end_number)
    min_step = 1
    max_step = 12
    step = randint(min_step, max_step)
    min_number_steps = 5
    max_number_steps = 10
    number_steps = randint(min_number_steps, max_number_steps)
    end_progression = start_progression + step * number_steps
    progression = (list(range(start_progression, end_progression, step)))
    first_element_progression = 0
    random_number = (randint(first_element_progression, number_steps - 1))
    answer = progression[random_number]
    progression[random_number] = '..'
    text = (str(progression))
    text2 = (text.replace("'", ""))
    text3 = (text2.replace(",", ""))
    text4 = (text3.replace("]", ""))
    text5 = (text4.replace("[", ""))
    question = text5
    return(question, answer)

print(caclulation())
