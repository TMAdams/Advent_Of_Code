#!/usr/bin/python3

# Script to solve day 4 of 2015 advent of code task

# Import python modules

import hashlib
import argparse

# Prepare function to parse CLI arguments


def parse_args():
    parser = argparse.ArgumentParser(description='Mine some AdventCoins')
    parser.add_argument('--input', required=True,
                        help='Input secret key')
    return parser.parse_args()

# Mine the first advent coin


def mine_coin_5(input: str):
    number = 0
    while True:
        number += 1
        string = input + str(number)
        hash = hashlib.md5(string.encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            break
    return str(number) + \
        ' is the solution needed to mine an AdventCoin with 5 zeros'


# Mine the second advent coin


def mine_coin_6(input: str):
    number = 0
    while True:
        number += 1
        string = input + str(number)
        hash = hashlib.md5(string.encode('utf-8')).hexdigest()
        if hash.startswith('000000'):
            break
    return str(number) + \
        ' is the solution needed to mine an AdventCoin with 6 zeros'

# Run analyses


def main():
    args = parse_args()
    input = args.input
    print(mine_coin_5(input))
    print(mine_coin_6(input))


if __name__ == '__main__':
    main()
