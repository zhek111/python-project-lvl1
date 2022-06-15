from prompt import string
from random import randint
from brain_games.games.greeting import name
manual = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def games():
    random_number = randint(1, 100)
    i = 1
    list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
            31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    while i <= 3:
        print(f'Question: {random_number}')
        answer = string('Your answer:  ')
        if random_number in list and answer == 'yes':
            print('Correct!')
            i = i + 1
            random_number = randint(1, 100)
        elif random_number not in list and answer == 'no':
            print('Correct!')
            i = i + 1
            random_number = randint(1, 100)
        elif random_number in list and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            return (f"Let's try again, {name}!")
        elif random_number not in list and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            return (f"Let's try again, {name}!")
    return(f'Congratulations, {name}!')
