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
    coord_string = str(x_coord) + ', ' + str(y_coord)
    coords_set = set()
    coords_set.add(coord_string)
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
        coord_string = str(x_coord) + ', ' + str(y_coord)
        coords_set.add(coord_string)
    house_count = len(coords_set)
    return str(house_count) + ' houses have at least one present delivered'

# Calculate how many presents now get delivered with Robo-Santa


def robo_houses(input: list):
    santa_x_coord = 0
    santa_y_coord = 0
    robo_x_coord = 0
    robo_y_coord = 0
    starting_coord = '0, 0'
    coord_set_2 = set()
    coord_set_2.add(starting_coord)
    instruction_count = 0
    for instruction in input:
        instruction_count += 1
        if instruction_count % 2 == 0:
            match instruction:
                case "^":
                    robo_y_coord += 1
                case ">":
                    robo_x_coord += 1
                case "v":
                    robo_y_coord -= 1
                case "<":
                    robo_x_coord -= 1
            robo_coord = str(robo_x_coord) + ', ' + str(robo_y_coord)
            coord_set_2.add(robo_coord)
        else:
            match instruction:
                case "^":
                    santa_y_coord += 1
                case ">":
                    santa_x_coord += 1
                case "v":
                    santa_y_coord -= 1
                case "<":
                    santa_x_coord -= 1
            santa_coord = str(santa_x_coord) + ', ' + str(santa_y_coord)
            coord_set_2.add(santa_coord)
    house_count_2 = len(coord_set_2)
    return str(house_count_2) + ' houses have at least one present delivered with \
    Robo-Santa helping out'

# Run analyses


def main():
    args = parse_args()
    input_str = open(args.input).readline().rstrip()
    input_list = []
    for item in input_str:
        input_list.append(item)
    print(total_houses(input_list))
    print(robo_houses(input_list))


if __name__ == '__main__':
    main()
