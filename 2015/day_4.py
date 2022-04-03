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

# Mine the advent coin


def mine_coin(input: str):
    number = 0
    while True:
        number += 1
        string = input + str(number)
        hash = hashlib.md5(string.encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            break
    return str(number) + ' is the solution needed to mine an AdventCoin'
