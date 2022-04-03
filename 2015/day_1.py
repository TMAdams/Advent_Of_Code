#!/usr/bin/python3

# Script to solve day 1 of 2015 advent of code task

# Import python modules

import argparse

# Prepare function to parse CLI arguments


def parse_args():
    parser = argparse.ArgumentParser(description='Decode Santas instructions')
    parser.add_argument('--input', required=True,
                        help='Input file containing coded instructions')
    return parser.parse_args()

# Prepare function to find final position


def final_position(input: list):
    for line in input:
        line = line.rstrip()
        Start = 0
        Up = line.count('(')
        Down = line.count(')')
        Floor = Start + Up - Down
        return 'Santa is on floor ' + str(Floor)

# Prepare function to find entrance to the basement


def basement_entry(input: list):
    for line in input:
        line = line.rstrip()
        Floor = 0
        Count = 0
        for instruction in line:
            Count += 1
            if instruction == '(':
                Floor += 1
            elif instruction == ')':
                Floor -= 1
            if Floor < 0:
                return 'Santa enters the basement at instruction ' + str(Count)
                break

# Run analyses


def main():
    args = parse_args()
    input = open(args.input).readlines()
    print(final_position(input))
    print(basement_entry(input))


if __name__ == '__main__':
    main()
