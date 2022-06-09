from prompt import string
name = string('May I have your name? ')
manual = 'Answer "yes" if the number is even, otherwise answer "no".'


def welcome_user():
    return (f'Hello, {name}!\n{manual}')
