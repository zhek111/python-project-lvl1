from prompt import string
from random import randint
from brain_games.games.greeting import name
from math import gcd
manual = 'Find the greatest common divisor of given numbers.'


def games():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    example1 = (f'{random_number1} {random_number2}')
    answer1 = gcd(random_number1, random_number2)
    list = [example1, answer1]
    question = list[0]
    correct_answer = list[1]
    i = 1
    while i <= 3:
        print(f'Question: {question}')
        answer = string('Your answer:  ')
        if str(correct_answer) == (answer):
            print('Correct!')
            i = i + 1
            random_number1 = randint(1, 100)
            random_number2 = randint(1, 100)
            example1 = (f'{random_number1} {random_number2}')
            answer1 = gcd(random_number1, random_number2)
            list = [example1, answer1]
            question = list[0]
            correct_answer = list[1]
        elif str(correct_answer) != (answer):
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again,{name}")
            i = 1
            random_number1 = randint(1, 100)
            random_number2 = randint(1, 100)
            example1 = (f'{random_number1} {random_number2}')
            answer1 = gcd(random_number1, random_number2)
            list = [example1, answer1]
            question = list[0]
            correct_answer = list[1]
    return(f'Congratulations, {name}!')
