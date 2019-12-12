#!/usr/bin/env python3

import re

# Each moon has a 3-dimensional position (x, y, and z) and a 3-dimensional velocity
# first update the velocity of every moon by applying gravity
#   consider every pair of moons.
#   On each axis (x, y, and z), the velocity of each moon changes by exactly +1 or -1 to pull the moons together
# Then, once all moons' velocities have been updated, update the position of every moon by applying velocity


class Moon:

    def __init__(self, pos_x, pox_y, pos_z):
        self.pos = [int(pos_x), int(pox_y), int(pos_z)]
        self.vel = [0, 0, 0]

    def shift_pos(self, index, amount):
        self.pos[index] += amount

    def shift_vel(self, index, amount):
        self.vel[index] += amount

    def position_update(self):
        for index in range(3):
            self.pos[index] += self.vel[index]

    def calc_energy(self):
        return sum(map(abs, self.pos)) * sum(map(abs, self.vel))


MOONS = []
STEP = 0


def parse(input):
    global MOONS
    for line in input:
        # e.g. <x=5, y=4, z=4>
        _, x, y, z, _ = re.split('<x=(.+), y=(.+), z=(.+)>', line)
        MOONS.append(Moon(x, y, z))


def velocity_compare(moon_a, moon_b):
    for index in range(3):
        if moon_a.pos[index] < moon_b.pos[index]:
            moon_a.shift_vel(index, 1)
            moon_b.shift_vel(index, -1)
        elif moon_b.pos[index] < moon_a.pos[index]:
            moon_b.shift_vel(index, 1)
            moon_a.shift_vel(index, -1)


def update_all_velocities():
    # A, B, C, D
    # A0 with B1
    # A0 with C2
    # A0 with D3
    # B1 with C2
    # B1 with D3
    # C2 with D3
    global MOONS
    velocity_compare(MOONS[0], MOONS[1])
    velocity_compare(MOONS[0], MOONS[2])
    velocity_compare(MOONS[0], MOONS[3])
    velocity_compare(MOONS[1], MOONS[2])
    velocity_compare(MOONS[1], MOONS[3])
    velocity_compare(MOONS[2], MOONS[3])


def update_all_positions():
    global MOONS
    for moon in MOONS:
        moon.position_update()


def total_energy():
    return sum(moon.calc_energy() for moon in MOONS)


def debug_status():
    print('Step: ' + str(STEP))
    for moon in MOONS:
        print('Pos: ' + str(moon.pos) + ' Vel: ' + str(moon.vel))
    print('---')


def moon_problem(input, steps, debug=True):
    global STEP
    parse(input)
    if debug:
        debug_status()
    for _ in range(steps):
        update_all_velocities()
        update_all_positions()
        STEP += 1
        if debug:
            debug_status()
    return total_energy()


if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        print(str(moon_problem(lines, 1000)))
