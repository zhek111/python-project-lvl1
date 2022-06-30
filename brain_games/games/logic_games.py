from prompt import string
CYCLES_COUNT = 3


def play_game(module):
    name = string('May I have your name? ')
    MANUAL = module.MANUAL
    (question, answer) = module.generate_round_game()
    print(f'Hello, {name}!\n{MANUAL}')
    i = 1
    while i <= CYCLES_COUNT:
        print(f'Question: {question}')
        your_answer = string('Your answer:  ')
        if your_answer == str(answer):
            print('Correct!')
            i = i + 1
            (question, answer) = module.generate_round_game()
        else:
            return(f"'{your_answer}' is wrong answer ;(. "
                   f"Correct answer was '{answer}'\n"
                   f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
