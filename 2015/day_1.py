#!/usr/bin/python3

# Script to solve day 1 of 2015 advent of code task

# Import python modules

import argparse

# Parse CLI arguments


def parse_args():
    parser = argparse.ArgumentParser(description=
                                     'Find out which floor Santa ends up on')
    parser.add_argument('--input', required=True,
                        help='Input file containing coded instructions')
    return parser.parse_args()
