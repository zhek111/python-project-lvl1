from prompt import string
name = string('May I have your name? ')


def games(manual, caclulation):
    print(f'Hello, {name}!\n{manual}')
    i = 1
    numbers_cycles = 3
    (question, answer) = caclulation()
    while i <= numbers_cycles:
        print(f'Question: {question}')
        your_answer = string('Your answer:  ')
        if your_answer == str(answer):
            print('Correct!')
            i = i + 1
            (question, answer) = caclulation()
        elif your_answer != str(answer):
            print(f"'{your_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'")
            return (f"Let's try again, {name}!")
    return(f'Congratulations, {name}!')
