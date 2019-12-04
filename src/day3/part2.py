#!/usr/bin/env python3

import re


def calc_coords(wire):
    current_coord = [0, 0]  # x,y
    coords = [[0,0]]
    for instruction in wire:
        direction, amount, _ = re.split('([0-9]+)', instruction)
        if direction == 'L':
            for x in range(1,int(amount)+1):
                coords.append(list([current_coord[0]-x,current_coord[1]]))
            current_coord[0] -= int(amount)
        elif direction == 'R':
            for x in range(1,int(amount)+1):
                coords.append(list([current_coord[0]+x,current_coord[1]]))
            current_coord[0] += int(amount)
        elif direction == 'U':
            for y in range(1, int(amount) + 1):
                coords.append(list([current_coord[0], current_coord[1]+y]))
            current_coord[1] += int(amount)
        elif direction == 'D':
            for y in range(1, int(amount) + 1):
                coords.append(list([current_coord[0], current_coord[1] - y]))
            current_coord[1] -= int(amount)
    return coords


def find_shortest_match(wire1_coords, wire2_coords):
    shortest = 9999
    wire1_dict = {}
    for idx1, w1 in enumerate(wire1_coords):
        if w1[0] not in wire1_dict:
            wire1_dict[w1[0]] = {}
        wire1_dict[w1[0]][w1[1]] = idx1

    for idx2, w2 in enumerate(wire2_coords):
        if w2[0] in wire1_dict:
            if w2[1] in wire1_dict[w2[0]]:
                dist = int(wire1_dict[w2[0]][w2[1]]) + int(idx2)
                if dist != 0 and dist < shortest:
                    shortest = dist
    return shortest


def cross_wires(wire1, wire2):
    wire1_coords = calc_coords(wire1)
    wire2_coords = calc_coords(wire2)
    return find_shortest_match(wire1_coords, wire2_coords)


if __name__ == '__main__':
    with open('input', 'r') as file:
        input = file.readlines()
        print('Result: ' + str(cross_wires(list(input[0].split(",")), list(input[1].split(",")))))

