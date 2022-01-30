#!/usr/bin/python3

# Script to solve day 1 of 2015 advent of code task

# Import python modules

import argparse

# Prepare function to parse CLI arguments


def parse_args():
    parser = argparse.ArgumentParser(description='Find out which floor Santa \
    ends up on')
    parser.add_argument('--input', required=True,
                        help='Input file containing coded instructions')
    return parser.parse_args()

# Prepare function to find final position


def final_position():
    for line in input:
        line = line.rstrip()
        Start = 0
        Up = line.count('(')
        Down = line.count(')')
        Floor = Start + Up - Down
        Statement = 'Santa is on ' + str(Floor)
        print(Statement)

# Run analyses


def main():
    args = parse_args()
    input = open(args.input).readlines()
    

if __name__ == '__main__':
    main()
