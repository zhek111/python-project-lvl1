#!/usr/bin/env python
from brain_games.games.logic_games import games
from brain_games.games.gcd_games import manual, caclulation


def main():
    print(games(manual, caclulation))


if __name__ == '__main__':
    main()
