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

# Calculate how many houses get presents


def total_houses(input: list):
    x_coord = 0
    y_coord = 0
    coord_string = x_coord + ', ' + y_coord
    coords_set = set()
    coords_set.append(coord_string)
    for instruction in input:
        match instruction:
            case "^":
                y_coord += 1
            case ">":
                x_coord += 1
            case "v":
                y_coord -= 1
            case "<":
                x_coord -= 1
        coord_string = x_coord + ', ' + y_coord
        coords_set.append(coord_string)
    house_count = len(coords_set)
    return str(house_count) + ' houses have at least one present delivered'

# Run analyses


def main():
    args = parse_args()
    input_str = open(args.input).readlines()
    input_list = []
    for item in input_str:
        input_list.append(item)
    print(total_houses(input_list))
