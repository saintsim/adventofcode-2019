#!/usr/bin/env python3

from src.day9 import boost_program as boost

if __name__ == '__main__':
    with open('input', 'r') as file:
        first_line = file.readlines()[0]
        input = list(map(int, first_line.split(",")))
        runner = boost.BoostProgram(input, [2])
        output = runner.run()
        print('Result: ' + str(output))
