#!/usr/bin/env python3

from src.day9 import boost_program as boost

'''
The springdroid will move forward automatically, constantly thinking about whether to jump. 
The springscript program defines the logic for this decision.

Two registers are available: T, the temporary value register, and J, the jump register. 
If the jump register is true at the end of the springscript program, the springdroid will try to jump. 
Both of these registers start with the value false.

they have a sensor that can detect whether there is ground at various distances in the direction it is facing; 
these values are provided in read-only registers

our springdroid can detect ground at four distances: one tile away (A), two tiles away (B), 
three tiles away (C), and four tiles away (D). If there is ground at the given distance, 
the register will be true; if there is a hole, the register will be false.

AND X Y sets Y to true if both X and Y are true; otherwise, it sets Y to false.
OR X Y sets Y to true if at least one of X or Y is true; otherwise, it sets Y to false.
NOT X Y sets Y to true if X is false; otherwise, it sets Y to false.

For example, the one-instruction program NOT A J means "if the tile immediately in front of me is not ground, jump".
'''


def instructions_to_ascii(instructions):
    asciis = []
    for i in instructions:
        asciis.append(int(ord(str(i))))
    return asciis


def get_input(_):
    input = 'NOT C J\n' \
            'NOT B T\n' \
            'OR T J\n' \
            'NOT A T\n' \
            'OR T J\n' \
            'AND D J\n' \
            'WALK\n'
    return instructions_to_ascii(input)


if __name__ == '__main__':
    with open('input', 'r') as file:
        first_line = file.readlines()[0]
        input = list(map(int, first_line.split(",")))
        runner = boost.BoostProgram(input, [], get_input, False, True)
        output = runner.run()

