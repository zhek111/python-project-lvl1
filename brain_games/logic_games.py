from random import randint
from prompt import string
from brain_games.greeting import name


def parity_check():
    random_number = randint(1, 100)
    i = 1
    while i <= 3:
        print(f'Question: {random_number}')
        answer = string('Your answer:  ')
        if random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
            i = i + 1
            random_number = randint(1, 100)
        elif random_number % 2 != 0 and answer == 'no':
            print('Correct!')
            i = i + 1
            random_number = randint(1, 100)
        elif random_number % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again,{name}")
            i = 1
            random_number = randint(1, 100)
        elif random_number % 2 != 0 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again,{name}")
            i = 1
            random_number = randint(1, 100)
    return(f'Congratulations, {name}!')
