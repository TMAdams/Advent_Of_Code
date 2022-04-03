#!/usr/bin/python3

# Script to solve day 3 of 2015 advent of code task

# Import python modules

import argparse

# Prepare function to parse CLI arguments


def parse_args():
    parser = argparse.ArgumentParser(description='Help Santa navigate')
    parser.add_argument('--input', required=True,
                        help='Input file containing directions')
    return parser.parse_args()
