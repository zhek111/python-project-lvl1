from prompt import string
from random import randint
from brain_games.games.greeting import name
manual = 'Answer "yes" if the number is even, otherwise answer "no".'


def games():
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
            return (f"Let's try again,{name}!")
        elif random_number % 2 != 0 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            return (f"Let's try again, {name}!")
    return(f'Congratulations, {name}!')
