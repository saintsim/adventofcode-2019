#!/usr/bin/env python3


def process_input(tokens):
    # [99] means that the program is finished
    # [1] adds together numbers read from two positions and stores the result in a third position
    #     The three integers immediately after the opcode tell you these three positions -
    #     the first two indicate the positions from which you should read the input values,
    #     and the third indicates the position at which the output should be stored.
    # [2] works exactly like opcode [1], except it multiplies the two inputs instead of adding them.
    #     Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.
    # --> Move to the next one by stepping forward 4 positions.
    for index in range(0, len(tokens), 4):
        element = tokens[index]
        if element == 99:
            return tokens[0]
        elif element == 1:
            tokens[tokens[index+3]] = tokens[tokens[index+1]] + tokens[tokens[index+2]]
        elif element == 2:
            tokens[tokens[index+3]] = tokens[tokens[index+1]] * tokens[tokens[index+2]]


def generate_inputs(default_input):
    for noun in range(0,100):
        for verb in range(0, 100):
            custom_input = list(default_input)
            custom_input[1] = noun
            custom_input[2] = verb
            if process_input(custom_input) == 19690720:
                return 100 * noun + verb


if __name__ == '__main__':
    with open('input', 'r') as file:
        input = file.readlines()[0]
        print('Result: ' + str(generate_inputs(list(map(int, input.split(","))))))
