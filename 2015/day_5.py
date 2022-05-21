#!/usr/bin/python3

# Script to solve day 5 of 2015 advent of code task

# Import python modules

import argparse

# Prepare function to parse CLI arguments


def parse_args():
    parser = argparse.ArgumentParser(description='Find out who is naughty \
    or nice')
    parser.add_argument('--input', required=True,
                        help='Input strings')
    return parser.parse_args()
