from random import randint
from random import choice
manual = 'What is the result of the expression?'


def caclulation():
    start_number = 1
    end_number = 100
    random_number1 = randint(start_number, end_number)
    random_number2 = randint(start_number, end_number)
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
    answer = randon_example[1]
    return(question, answer)
