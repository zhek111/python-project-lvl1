#!/usr/bin/env python
from brain_games.games.logic_games import games
from brain_games.games.even_games import manual, caclulation, question, answer


def main():
    print(games(manual, question, answer))


if __name__ == '__main__':
    main()
