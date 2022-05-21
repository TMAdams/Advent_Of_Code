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

# Identify nice strings


def find_nice_string(input: list):
    nice_strings = set()
    for string in list:
        # First, set the default result for each test
        vowel_test = 'N'
        bad_test = 'Y'
        duplicate_test = 'N'
        # Then test for vowels
        a_count = string.count('a')
        e_count = string.count('e')
        i_count = string.count('i')
        o_count = string.count('o')
        u_count = string.count('u')
        if a_count + e_count + i_count + o_count + u_count >= 3:
            vowel_test = 'Y'
        # Next test for presence of bad strings
        if 'ab' or 'cd' or 'pq' or 'xy' in string:
            bad_test = 'N'
        # Finally test for duplicates character
        character_list = []
        for character in string:
            string_length = len(string)
            character_list.append(character)
        for number in range(string_length):
            if character_list[number] == character_list[number + 1]:
                duplicate_test = 'Y'
        if vowel_test == 'Y' and bad_test == 'N' and duplicate_test == 'Y':
            nice_strings.add(string)
    nice_count = len(nice_strings)
    return str(nice_count) + ' strings are nice'

# Run analysis


def main():
    args = parse_args()
    input = open(args.input).readlines()
    print(find_nice_string(input))


if __name__ == '__main__':
    main()
