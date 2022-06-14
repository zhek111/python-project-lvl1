#!/usr/bin/env python
from brain_games.games.greeting import welcome_user
from brain_games.games.parity_games import games, manual


def main():
    print(welcome_user(manual))
    print(games())


if __name__ == '__main__':
    main()
