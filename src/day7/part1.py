#!/usr/bin/env python3

import itertools
from src.day5 import part2

# Amp: A, B, C, D, E
# phase setting: 0, 1, 2, 3 4 (not sure which amp gets which, but each use one)
# input: 0 (for amp A), amp B takes amp A's output as input etc.
# each amp runs the test input fresh


def get_phase_setting_combinations(range_from, range_to):
    #  e.g. for 0, 1, 2 = 0,1,2 ; 1,0,2 ; 2,0.1
    number_range = range(range_from, range_to)
    return list(itertools.permutations(number_range, len(number_range)))


def amplification(input):
    number_of_amps = 5
    phase_settings = get_phase_setting_combinations(0, number_of_amps)
    max_result = 0
    for setting in phase_settings:
        user_input = 0
        result = 0
        for amp in range(0, number_of_amps):
            result = part2.diagnostic_program(input, [setting[amp], user_input])
            user_input = result
        if result > max_result:
            max_result = result
    return max_result


if __name__ == '__main__':
    with open('input', 'r') as file:
        input = file.readlines()[0]
        print('Result: ' + str(amplification(list(map(int, input.split(","))))))
