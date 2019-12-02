#!/usr/bin/env python3


def fuel_required(lines):
    # divide by three, round down, and subtract 2.
    fuel_required = 0
    for line in lines:
        fuel_required = fuel_required + int(int(line)/3)-2
    return fuel_required


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        print('Result: ' + str(fuel_required(lines)))
