#!/usr/bin/env python
from brain_games.games.prime_games import calculate
from brain_games.games.calc_games import tune


def main():
    tune(calculate)


if __name__ == '__main__':
    main()
