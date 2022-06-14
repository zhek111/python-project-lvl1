from prompt import string
name = string('May I have your name? ')


def welcome_user(manual):
    return (f'Hello, {name}!\n{manual}')
