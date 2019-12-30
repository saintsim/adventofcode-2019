#!/usr/bin/env python3

from src.day9 import boost_program as boost
import re
import random
import itertools

'''
Movement via north, south, east, or west.
* To take an item the droid sees in the environment, use the command take <name of item>.
    For example, if the droid reports seeing a red ball, you can pick it up with take red ball.
* To drop an item the droid is carrying, use the command drop <name of item>.
    For example, if the droid is carrying a green ball, you can drop it with drop green ball.
* To get a list of all of the items the droid is currently carrying, use the command inv (for "inventory").
'''

SPACE = ord(' ')
NEW_LINE = ord('\n')
DASH = ord('-')

BAD_ITEMS = ['photons', 'giant electromagnet', 'escape pod', 'molten lava', 'infinite loop']
ITEMS_HELD = []
WEIGHT_INDEX = 0
WEIGHT_COMMAND_INDEX = 0
WEIGHT_COMBINATIONS = []
WEIGHT_COMMANDS_FOR_INDEX = dict()

LAST_OUTPUT_INDEX = 0
PAST_MOVEMENTS_BY_PLACE = dict()
PAST_MOVEMENT_OPTIONS = []
LAST_PLACE = ''


def give_instruction(instruction):
    instruction_to_give = []
    for letter in instruction:
        instruction_to_give.append(ord(letter))
    instruction_to_give.append(NEW_LINE)
    return instruction_to_give


def make_movement_decision(place, movement_options):
    global PAST_MOVEMENTS
    movements_to_avoid = set()
    if not len(movement_options):
        movement_options = PAST_MOVEMENT_OPTIONS
    if place in PAST_MOVEMENTS_BY_PLACE:
        movements_to_avoid = PAST_MOVEMENTS_BY_PLACE[place]
    for movement in movement_options:
        if movement not in movements_to_avoid:
            return movement
    # we got here which means we've exhausted all past movements
    # so let's take the first one again and reset the movement list
    PAST_MOVEMENTS = set()
    return random.choice(movement_options)


def get_weight_combinations(items):
    combinations = []
    for i in range(1,len(items)+1):
        for l in list(itertools.combinations(items, i)):
            combinations.append(l)
    return combinations


def command_for_combination(combination, items):
    commands = []
    for item_needed in combination:
        if item_needed not in items:
            commands.append('take ' + item_needed)
    for item_holding in items:
        if item_holding not in combination:
            commands.append('drop ' + item_holding)
    commands.append('south')
    return commands


def adjust_weight(weight_index, command_index):
    #  we're in the security checkpoint about to head south
    # drop some things
    global WEIGHT_COMBINATIONS, WEIGHT_COMMANDS_FOR_INDEX, WEIGHT_COMMAND_INDEX
    if not len(WEIGHT_COMBINATIONS):
        WEIGHT_COMBINATIONS = get_weight_combinations(ITEMS_HELD)
    if str(weight_index) not in WEIGHT_COMMANDS_FOR_INDEX:
        WEIGHT_COMMANDS_FOR_INDEX[str(weight_index)] = command_for_combination(WEIGHT_COMBINATIONS[weight_index], ITEMS_HELD)
    next_command = WEIGHT_COMMANDS_FOR_INDEX[str(weight_index)][command_index]
    if WEIGHT_COMMAND_INDEX+1 == len(WEIGHT_COMMANDS_FOR_INDEX[str(weight_index)]):
        WEIGHT_COMMAND_INDEX = -1
    else:
        WEIGHT_COMMAND_INDEX += 1
    return next_command


def adjust_inventory(command):
    if command.startswith('take'):
        _, item, _ = re.split('take (.+)', command)
        ITEMS_HELD.append(item)
    elif command.startswith('drop'):
        _, item, _ = re.split('drop (.+)', command)
        ITEMS_HELD.remove(item)


def reset_weight_variables():
    global WEIGHT_INDEX, WEIGHT_COMMAND_INDEX, WEIGHT_COMBINATIONS, WEIGHT_COMMANDS_FOR_INDEX
    WEIGHT_INDEX = 0
    WEIGHT_COMMAND_INDEX = 0
    WEIGHT_COMBINATIONS = []
    WEIGHT_COMMANDS_FOR_INDEX = dict()


def make_command_decision(place, movement_options, items):
    global PAST_MOVEMENT_OPTIONS, PAST_MOVEMENTS_BY_PLACE, ITEMS_HELD, WEIGHT_INDEX
    # it's time to prepare for the weigh in
    if place == 'Security Checkpoint':
        if WEIGHT_INDEX == 0:
            WEIGHT_INDEX = len(items)
        next_command = adjust_weight(WEIGHT_INDEX, WEIGHT_COMMAND_INDEX)
        if WEIGHT_COMMAND_INDEX == -1:
            WEIGHT_INDEX -= 1
        print(next_command)
        adjust_inventory(next_command)
        return next_command
    else:
        reset_weight_variables()
        if len(movement_options):
            PAST_MOVEMENT_OPTIONS = movement_options
        for item in items:
            if item not in BAD_ITEMS:
                print('Taking: ', items[0])
                ITEMS_HELD.append(items[0])
                return 'take ' + items[0]
        movement_decision = make_movement_decision(place, movement_options)
        if place in PAST_MOVEMENTS_BY_PLACE:
            PAST_MOVEMENTS_BY_PLACE[place].add(movement_decision)
        else:
            PAST_MOVEMENTS_BY_PLACE[place] = set([movement_decision])
        print('Moving: ', movement_decision)
        return movement_decision


def parse(lines):
    movement_options = []
    movement_options_record = False
    items = []
    items_record = False
    place = ''
    for line in lines:
        if line.startswith('=='):
            _, place, _ = re.split('== (.+) ==', line)
        elif line == 'Doors here lead:':
            movement_options_record = True
        elif line == 'Items here:':
            items_record = True
        elif movement_options_record is True:
            if len(line):
                _, movement, _ = re.split('- (.+)', line)
                movement_options.append(movement)
            else:
                movement_options_record = False
        elif items_record is True:
            if len(line):
                _, item, _ = re.split('- (.+)', line)
                items.append(item)
            else:
                items_record = False
    global LAST_PLACE
    if len(place):
        LAST_PLACE = place
    else:
        place = LAST_PLACE
    return place, movement_options, items


def print_droid(output):
    global LAST_OUTPUT_INDEX
    word = ''
    lines = []
    for index, out_char in enumerate(output):
        if index > LAST_OUTPUT_INDEX:
            if out_char == NEW_LINE:
                lines.append(word)
                word = ''
            else:
                word += str(chr(out_char))
    LAST_OUTPUT_INDEX = len(output)-1
    place, movement_options, items = parse(lines)
    instruction = make_command_decision(place, movement_options, items)
    return give_instruction(instruction)


if __name__ == '__main__':
    with open('input', 'r') as file:
        first_line = file.readlines()[0]
        input = list(map(int, first_line.split(",")))
        runner = boost.BoostProgram(input, [], print_droid, False, True)
        output = runner.run()
