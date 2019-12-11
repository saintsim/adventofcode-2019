#!/usr/bin/env python3


class BoostProgram:

    def __init__(self, input, initial_inputs):
        # tokens up to input size + a dictionary for overflow
        self.tokens = list(input)
        self.overflow_tokens = {}

        # inputs and outputs storage
        self.inputs = []
        self.add_inputs(initial_inputs)
        self.outputs = []

        # keep track of the index and relative base
        self.relative_base = 0

    def add_inputs(self, inputs):
        for input in inputs:
            self.inputs.append(input)

    @staticmethod
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

    def write_token(self, location_to_write_to, contents):
        if location_to_write_to < len(self.tokens):
            self.tokens[location_to_write_to] = contents
        else:
            self.overflow_tokens[str(location_to_write_to)] = contents

    def read_token(self, location):
        if location < len(self.tokens):
            return self.tokens[location]
        elif str(location) in self.overflow_tokens:
            return self.overflow_tokens[str(location)]
        else:
            return 0

    def get_token(self, location, mode):
        if mode == 1:
            # immediate mode
            return self.read_token(location)
        elif mode == 0:
            # position mode
            # if location > len(TOKENS):
            #    return 0
            return self.read_token(self.read_token(location))
        elif mode == 2:
            # relative mode
            out = self.read_token(self.read_token(location) + self.relative_base)
            return out
        else:
            Exception('unknown mode')

    def run(self):
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
        print_num = 1
        while True:
            element = self.read_token(index)
            print(str(print_num) + 'El -> ' + str(element))
            print_num += 1
            a_mode, b_mode, c_mode, opcode = self.token_parse(element)
            if opcode == 99:
                print('halting -->')
                return self.outputs
            elif opcode == 1:
                if a_mode == 2:
                    self.write_token(self.read_token(index + 3) + self.relative_base,
                                     self.get_token(index + 1, c_mode) + self.get_token(index + 2, b_mode))
                else:
                    self.write_token(self.read_token(index+3),
                                     self.get_token(index+1, c_mode) + self.get_token(index+2, b_mode))
                index += 4
            elif opcode == 2:
                if a_mode == 2:
                    self.write_token(self.read_token(index+3) + self.relative_base,
                                     self.get_token(index+1, c_mode) * self.get_token(index+2, b_mode))
                else:
                    self.write_token(self.read_token(index+3),
                                     self.get_token(index+1, c_mode) * self.get_token(index+2, b_mode))

                index += 4
            elif opcode == 3:  # magic input number
                if c_mode == 2:
                    self.write_token(self.read_token(index + 1) + self.relative_base, 1)
                else:
                    self.write_token(self.read_token(self.read_token(index+1)), 1)
                index += 2
            elif opcode == 4:
                to_print = self.get_token(index+1, c_mode)
                self.outputs.append(to_print)
                print(to_print)
                index += 2
            elif opcode == 5:
                first_param = self.get_token(index+1, c_mode)
                if first_param != 0:
                    index = self.get_token(index+2, b_mode)
                else:
                    index += 3
            elif opcode == 6:
                first_param = self.get_token(index+1, c_mode)
                if first_param == 0:
                    index = self.get_token(index+2, b_mode)
                else:
                    index += 3
            elif opcode == 7:
                first_param = self.get_token(index + 1, c_mode)
                second_param = self.get_token(index + 2, b_mode)
                if a_mode == 2:
                    self.write_token(self.read_token(index + 3) + self.relative_base,
                                     1 if first_param < second_param else 0)
                else:
                    self.write_token(self.read_token(index+3), 1 if first_param < second_param else 0)
                index += 4
            elif opcode == 8:
                first_param = self.get_token(index + 1, c_mode)
                second_param = self.get_token(index + 2, b_mode)
                if c_mode == 2:
                    self.write_token(self.read_token(index + 3) + self.relative_base,
                                     1 if first_param == second_param else 0)
                else:
                    self.write_token(self.read_token(index + 3),
                                     1 if first_param == second_param else 0 )
                index += 4
            elif opcode == 9:
                first_param = self.get_token(index + 1, c_mode)
                try:
                    self.relative_base += first_param
                except:
                    pass
                # print('new RELATIVE_BASE: (' + str(first_param) + ') = ' + str(RELATIVE_BASE))
                index += 2
