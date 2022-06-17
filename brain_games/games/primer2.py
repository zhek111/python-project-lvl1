from unicodedata import name
from primer import random_number


def games():
    i = 1
    while i <= 3:
        name = random_number() 
        name2 = 'ggg'
        i = i + 1
        return name, name2


(question, answer) = games()
