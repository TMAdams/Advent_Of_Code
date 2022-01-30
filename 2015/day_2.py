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

# Calculate total area of paper needed


def total_paper(input: list):
    packages = []
    for line in input:
        line = line.rstrip()
        dimensions = line.split('x')
        area_1 = dimensions[0] * dimensions[1]
        area_2 = dimensions[0] * dimensions[2]
        area_3 = dimensions[1] * dimensions[2]
        areas_list = [area_1, area_2, area_3]
        areas_list.sort()
        package_area = (2 * area_1) + (2 * area_2) + (2 * area_3) + \
            areas_list[0]
        packages.append(package_area)
    total_area = sum(packages)
    return 'The elves require ' + total_area + ' square feet of wrapping paper'

# Run analyses


def main():
    args = parse_args()
    input = open(args.input).readlines()
    print(total_paper(input))


if __name__ == '__main__':
    main()
