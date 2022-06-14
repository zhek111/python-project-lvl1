from prompt import string
from random import randint
from brain_games.games.greeting import name
manual = 'What number is missing in the progression?'


def games():
    start_progression = randint(1, 100)
    step = randint(1, 12)
    number_steps = randint(5, 10)
    end_progression = start_progression + step * number_steps
    progression = (list(range(start_progression, end_progression, step)))
    random_number = (randint(0, number_steps - 1))
    correct_answer = progression[random_number]
    progression[random_number] = '..'
    text = (str(progression))
    text2 = (text.replace("'", ""))
    text3 = (text2.replace(",", ""))
    question = text3
    i = 1
    while i <= 3:
        print(f'Question: {question}')
        answer = string('Your answer:  ')
        if str(correct_answer) == (answer):
            print('Correct!')
            i = i + 1
            start_progression = randint(1, 100)
            step = randint(1, 12)
            number_steps = randint(5, 10)
            end_progression = start_progression + step * number_steps
            progression = (list(range(start_progression, end_progression, step)))
            random_number = (randint(0, number_steps - 1))
            correct_answer = progression[random_number]
            progression[random_number] = '..'
            text = (str(progression))
            text2 = (text.replace("'", ""))
            text3 = (text2.replace(",", ""))
            question = text3
        elif str(correct_answer) != (answer):
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again,{name}")
            i = 1
            start_progression = randint(1, 100)
            step = randint(1, 12)
            number_steps = randint(5, 10)
            end_progression = start_progression + step * number_steps
            progression = (list(range(start_progression, end_progression, step)))
            random_number = (randint(0, number_steps - 1))
            correct_answer = progression[random_number]
            progression[random_number] = '..'
            text = (str(progression))
            text2 = (text.replace("'", ""))
            text3 = (text2.replace(",", ""))
            question = text3
    return(f'Congratulations, {name}!')
