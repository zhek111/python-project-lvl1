from prompt import string
import calc_games

def play_game(module):
    name = string('May I have your name? ')
    MANUAL = module.MANUAL
    (question, answer) = module.generate_round_game()
    print(f'Hello, {name}!\n{MANUAL}')
    i = 1
    numbers_cycles = 3
    while i <= numbers_cycles:
        print(f'Question: {question}')
        your_answer = string('Your answer:  ')
        if your_answer == str(answer):
            print('Correct!')
            i = i + 1
            (question, answer) = module.generate_round_game()
        elif your_answer != str(answer):
            print(f"'{your_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'\n"
                  f"Let's try again, {name}!")
            return False
    print(f'Congratulations, {name}!')
    return True


print(play_game(calc_games))
