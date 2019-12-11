#!/usr/bin/env python3


TOKENS = []
RELATIVE_BASE = 0


def token_parse(token):
    # ABCDE
    #  1002
    # DE - two-digit opcode
    # C - mode of 1st parameter
    # B - mode of 2nd parameter
    # A - mode of 3rd parameter
    # mode is either 0 for position mode (day2 default) or 1 for immediate mode
    # or 2 for relative mode (day 9 feature!)
    a_mode = b_mode = c_mode = 0
    token_str = str(token)
    opcode = token_str[-2:]
    if len(token_str) > 2:
        c_mode = token_str[-3:-2]

    if len(token_str) > 3:  # e.g. 1002
       b_mode = token_str[-4:-3]

    if len(token_str) > 4:  # e.g. 11002
       c_mode = token_str[-5:-4]

    if len(token_str) > 5:
        raise ValueError(
            "token is longer than 5 chars, looks wrong")

    return int(a_mode), int(b_mode), int(c_mode), int(opcode)


def get_token(location, mode):
    try:
        if mode == 1:
            # immediate mode
            return int(location)
        elif mode == 0:
            # position mode
            #if location > len(TOKENS):
            #    return 0
            return int(TOKENS[location])
        elif mode == 2:
            # relative mode
            #print('RELATIVE_BASE: ' + str(RELATIVE_BASE))
            #location_to_look = int(TOKENS[location]) + int(RELATIVE_BASE)
            #if location_to_look > len(TOKENS):
            #    return 0
            out = TOKENS[location+RELATIVE_BASE]
            if out == None:
                pass
            return out
        else:
            Exception('unkown mode')
    except:
        pass


# relative mode:
#  they count from a value called the relative base. The relative base starts at 0.
#  The address a relative mode parameter refers to is itself plus the current relative base
#  (When the relative base is 0, relative mode parameters and
#  position mode parameters with the same value refer to the same address.)
# For example, given a relative base of 50, a relative mode parameter of -7
#   refers to memory address 50 + -7 = 43.


def boost_program(input, user_inputs):
    global TOKENS
    global RELATIVE_BASE
    TOKENS = input

    for i in range(9999):
        TOKENS.append(0)

    # [99] means that the program is finished
    # [1] adds together numbers read from two positions and stores the result in a third position
    #     The three integers immediately after the opcode tell you these three positions -
    #     the first two indicate the positions from which you should read the input values,
    #     and the third indicates the position at which the output should be stored.
    # [2] works exactly like opcode [1], except it multiplies the two inputs instead of adding them.
    #     Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.
    # [3] takes a single integer as input and saves it to the position given by its only parameter.
    #     For example, the instruction 3,50 would take an input value and store it at address 50.
    # [4] outputs the value of its only parameter. For example,
    #     the instruction 4,50 would output the value at address 50.
    # [5] is jump-if-true: if the first parameter is non-zero,
    #     it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    # [6] is jump-if-false: if the first parameter is zero,
    #     it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
    # [7] is less than: if the first parameter is less than the second parameter,
    #     it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    # [8] is equals: if the first parameter is equal to the second parameter,
    #     it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
    # [9] Opcode 9 adjusts the relative base by the value of its only parameter.
    #      The relative base increases (or decreases, if the value is negative)
    #      by the value of the parameter.
    index = 0
    output = ''
    while True:
        element = TOKENS[index]
        # print('El -> ' + str(element))
        a_mode, b_mode, c_mode, opcode = token_parse(element)
        shift = 0
        if opcode == 99:
            print('halting -->')
            return output
        elif opcode == 1:
            if a_mode == 2:
                TOKENS[TOKENS[index + 3]+int(RELATIVE_BASE)] = get_token(TOKENS[index + 1], c_mode) + get_token(TOKENS[index + 2], b_mode)
            else:
                TOKENS[TOKENS[index+3]] = get_token(TOKENS[index+1], c_mode) + get_token(TOKENS[index+2], b_mode)
            shift = 4
        elif opcode == 2:
            if a_mode == 2:
                TOKENS[TOKENS[index + 3] + int(RELATIVE_BASE)] = get_token(TOKENS[index + 1], c_mode) * get_token(TOKENS[index + 2], b_mode)
            else:
                TOKENS[TOKENS[index+3]] = get_token(TOKENS[index+1], c_mode) * get_token(TOKENS[index+2], b_mode)
            shift = 4
        elif opcode == 3:  # magic input number
            if c_mode == 2:
                rangep = TOKENS[index + 1] + int(RELATIVE_BASE)
                if rangep > len(TOKENS):
                    pass
                TOKENS[rangep] = 1
            else:
                TOKENS[TOKENS[index+1]] = 1
            shift = 2
        elif opcode == 4:
            to_print = get_token(TOKENS[index+1], c_mode)
            output = to_print
            print(to_print)
            shift = 2
        elif opcode == 5:
            first_param = get_token(TOKENS[index+1], c_mode)
            if first_param != 0:
                index = get_token(TOKENS[index+2], b_mode)
            else:
                shift = 3
        elif opcode == 6:
            first_param = get_token(TOKENS[index+1], c_mode)
            if first_param == 0:
                index = get_token(TOKENS[index+2], b_mode)
            else:
                shift = 3
        elif opcode == 7:
            first_param = get_token(TOKENS[index + 1], c_mode)
            second_param = get_token(TOKENS[index + 2], b_mode)
            if a_mode == 2:
                TOKENS[TOKENS[index + 3]+int(RELATIVE_BASE)] = 1 if first_param < second_param else 0
            else:
                TOKENS[TOKENS[index + 3]] = 1 if first_param < second_param else 0
            shift = 4
        elif opcode == 8:
            first_param = get_token(TOKENS[index + 1], c_mode)
            second_param = get_token(TOKENS[index + 2], b_mode)
            if c_mode == 2:
                TOKENS[TOKENS[index + 3]+int(RELATIVE_BASE)] = 1 if first_param == second_param else 0
            else:
                TOKENS[TOKENS[index + 3]] = 1 if first_param == second_param else 0
            shift = 4
        elif opcode == 9:
            first_param = get_token(TOKENS[index + 1], c_mode)
            try:
                RELATIVE_BASE += first_param
            except:
                pass
            # print('new RELATIVE_BASE: (' + str(first_param) + ') = ' + str(RELATIVE_BASE))
            shift = 2
        index += shift


if __name__ == '__main__':
    with open('test_input2', 'r') as file:
        input = file.readlines()[0]
        print('Result: ' + str(boost_program(list(map(int, input.split(","))), [1])))
