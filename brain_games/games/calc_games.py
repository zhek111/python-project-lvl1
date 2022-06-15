from prompt import string
from random import randint
from random import choice
from brain_games.games.greeting import name
manual = 'What is the result of the expression?'


def games():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    example1 = (f'{random_number1} + {random_number2}')
    answer1 = random_number1 + random_number2
    list1 = [example1, answer1]
    example2 = (f'{random_number1} - {random_number2}')
    answer2 = random_number1 - random_number2
    list2 = [example2, answer2]
    example3 = (f'{random_number1} * {random_number2}')
    answer3 = random_number1 * random_number2
    list3 = [example3, answer3]
    randon_example = choice([list1, list2, list3])
    question = randon_example[0]
    correct_answer = randon_example[1]
    i = 1
    while i <= 3:
        print(f'Question: {question}')
        answer = string('Your answer:  ')
        if str(correct_answer) == (answer):
            print('Correct!')
            i = i + 1
            random_number1 = randint(1, 100)
            random_number2 = randint(1, 100)
            example1 = (f'{random_number1} + {random_number2}')
            answer1 = random_number1 + random_number2
            list1 = [example1, answer1]
            example2 = (f'{random_number1} - {random_number2}')
            answer2 = random_number1 - random_number2
            list2 = [example2, answer2]
            example3 = (f'{random_number1} * {random_number2}')
            answer3 = random_number1 * random_number2
            list3 = [example3, answer3]
            randon_example = choice([list1, list2, list3])
            question = randon_example[0]
            correct_answer = randon_example[1]
        elif str(correct_answer) != (answer):
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'")
            print(f"Let's try again,{name}")
            i = 1
            random_number1 = randint(1, 100)
            random_number2 = randint(1, 100)
            example1 = (f'{random_number1} + {random_number2}')
            answer1 = random_number1 + random_number2
            list1 = [example1, answer1]
            example2 = (f'{random_number1} - {random_number2}')
            answer2 = random_number1 - random_number2
            list2 = [example2, answer2]
            example3 = (f'{random_number1} * {random_number2}')
            answer3 = random_number1 * random_number2
            list3 = [example3, answer3]
            randon_example = choice([list1, list2, list3])
            question = randon_example[0]
            correct_answer = randon_example[1]
    return(f'Congratulations, {name}!')
