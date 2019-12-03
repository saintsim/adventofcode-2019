#!/usr/bin/env python3

import re


def calc_coords(wire):
    coords = []
    current_coord = [0, 0]  # x,y
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
    shortest = -1
    w1_shortest = []
    for w1 in wire1_coords:
        dist = abs(w1[0]) + abs(w1[1])
        if dist < 999:
            w1_shortest.append(list(w1))
    w2_shortest = []
    for w2 in wire2_coords:
        dist = abs(w2[0]) + abs(w2[1])
        if dist < 999:
            w2_shortest.append(list(w2))
    for w1 in w1_shortest:
        for w2 in w2_shortest:
            if int(w1[0]) == int(w2[0]) and int(w1[1]) == int(w2[1]):
                dist = abs(w1[0]) + abs(w1[1])
                if shortest == -1 or dist < shortest:
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

