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
    text4 = (text3.replace("]", ""))
    text5 = (text4.replace("[", ""))
    question = text5
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
            progression = (list(range(start_progression,
                                      end_progression, step)))
            random_number = (randint(0, number_steps - 1))
            correct_answer = progression[random_number]
            progression[random_number] = '..'
            text = (str(progression))
            text2 = (text.replace("'", ""))
            text3 = (text2.replace(",", ""))
            text4 = (text3.replace("]", ""))
            text5 = (text4.replace("[", ""))
            question = text5
        elif str(correct_answer) != (answer):
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            return (f"Let's try again, {name}!")
    return(f'Congratulations, {name}!')
