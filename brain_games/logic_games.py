from prompt import string
CYCLES_COUNT = 3


def play_game(game):
    name = string('May I have your name? ')
    (question, answer) = game.generate_round_game()
    print(f'Hello, {name}!')
    print(f'{game.MANUAL}')
    i = 1
    while i <= CYCLES_COUNT:
        print(f'Question: {question}')
        your_answer = string('Your answer:  ')
        if your_answer == (answer):
            print('Correct!')
            i = i + 1
            (question, answer) = game.generate_round_game()
        else:
            print(f"'{your_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
