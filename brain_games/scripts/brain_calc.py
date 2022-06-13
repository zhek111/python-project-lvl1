#!/usr/bin/env python
from brain_games.games.greeting_calc import welcome_user
from brain_games.games.calc_games import games


def main():
    print(welcome_user())
    print(games())


if __name__ == '__main__':
    main()
