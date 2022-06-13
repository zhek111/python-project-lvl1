#!/usr/bin/env python
from brain_games.games.greeting import welcome_user
from brain_games.games.logic_games import parity_check


def main():
    print(welcome_user())
    print(parity_check())


if __name__ == '__main__':
    main()
