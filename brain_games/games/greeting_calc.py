from prompt import string
name = string('May I have your name? ')
manual = 'What is the result of the expression?'


def welcome_user():
    return (f'Hello, {name}!\n{manual}')
