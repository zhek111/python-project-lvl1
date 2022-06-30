#!/usr/bin/env python
from brain_games.games import calc_games
from brain_games.games.logic_games import play_game


def main():
    play_game(calc_games)


if __name__ == '__main__':
    main()
