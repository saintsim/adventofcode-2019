#!/usr/bin/env python3


def fuel_required(lines):
    # divide by three, round down, and subtract 2.
    total_fuel_required = 0
    for line in lines:
        fuel_required = line
        while True:
            fuel_required = int(int(fuel_required)/3)-2
            if fuel_required < 0:
                break
            total_fuel_required = total_fuel_required + fuel_required
    return total_fuel_required


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        print('Result: ' + str(fuel_required(lines)))
