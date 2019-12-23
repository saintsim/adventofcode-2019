#!/usr/bin/env python3

from src.day23 import computer_program


def make_network(input, number_of_computers):
    computers = []
    nat = []
    given = {}
    for i in range(number_of_computers):
        this_computer = computer_program.ComputerProgram(input, [i], False, False)
        this_computer.start()
        computers.append(this_computer)
    while True:
        finished = True
        all_empty = True
        for computer in computers:
            if computer.state != 'finished':
                finished = False
            if len(computer.outputs) > 2:
                dest_comput = computer.outputs.pop(0)
                new_inputs = [computer.outputs.pop(0), computer.outputs.pop(0)]
                if dest_comput == 255:
                    nat = list(new_inputs)
                else:
                    computers[dest_comput].add_inputs(new_inputs)
                    if computers[dest_comput].state == 'needs input':
                        computers[dest_comput].start()
            if computer.state == 'needs input':
                computer.add_inputs([-1])
                computer.start()
            else:
                all_empty = False
        if all_empty and len(nat):
            y_value = str(nat[1])
            # print('Delivering: ', nat)
            if y_value in given:
                print('y: ', y_value)
                return y_value
            else:
                given[y_value] = 1
            computers[0].add_inputs(nat)
            nat = []
        if finished:
            break


if __name__ == '__main__':
    with open('input', 'r') as file:
        first_line = file.readlines()[0]
        input = list(map(int, first_line.split(",")))
        print(str(make_network(input, 50)))

