#!/usr/bin/python3

# Script to solve day 2 of 2015 advent of code task

# Import python modules

import argparse

# Prepare function to parse CLI arguments


def parse_args():
    parser = argparse.ArgumentParser(description='Help elves with wrapping')
    parser.add_argument('--input', required=True,
                        help='Input file containing present dimensions')
    return parser.parse_args()
