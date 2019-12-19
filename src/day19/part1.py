#!/usr/bin/env python3

from src.day9 import boost_program as boost


if __name__ == '__main__':
    with open('input', 'r') as file:
        first_line = file.readlines()[0]
        input = list(map(int, first_line.split(",")))
        count = 0
        for y in range(0, 50):
            line = ''
            for x in range(0, 50):
                pgm = boost.BoostProgram(input, [x, y])
                output = pgm.run()
                for o in output:
                    line += str(o)
                    if str(o) == '1':
                        count += 1
            print(line)
        print('Result: ' + str(count))
