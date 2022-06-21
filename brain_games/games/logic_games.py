from prompt import string


def tune(calculate):
    name = string('May I have your name? ')
    (question, answer, MANUAL) = calculate()
    print(f'Hello, {name}!\n{MANUAL}')
    i = 1
    numbers_cycles = 3
    while i <= numbers_cycles:
        print(f'Question: {question}')
        your_answer = string('Your answer:  ')
        if your_answer == str(answer):
            print('Correct!')
            i = i + 1
            (question, answer, MANUAL) = calculate()
        elif your_answer != str(answer):
            return(f"'{your_answer}' is wrong answer ;(. "
                   f"Correct answer was '{answer}'\n"
                   f"Let's try again, {name}!")
    return(f'Congratulations, {name}!')
