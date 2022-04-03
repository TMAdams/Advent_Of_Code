#!/usr/bin/python3

# Script to solve day 4 of 2015 advent of code task

# Import python modules

import hashlib
import argparse

# Prepare function to parse CLI arguments


def parse_args():
    parser = argparse.ArgumentParser(description='Mine some advent coins')
    parser.add_argument('--input', required=True,
                        help='Input secret key')
    return parser.parse_args()
