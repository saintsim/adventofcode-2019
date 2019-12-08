#!/usr/bin/env python3

import collections


def find_pixels(pixels):
    size_x = 25
    size_y = 6
    area = size_x * size_y
    pixel_index = 0
    zero_count = 99
    least_zero_layer = []
    while pixel_index < len(pixels):
        layer = []
        while len(layer) < area:
            layer.append(pixels[pixel_index])
            pixel_index += 1
        counter = collections.Counter(layer)
        if counter['0'] < zero_count:
            least_zero_layer = counter
            zero_count = counter['0']
    return int(least_zero_layer['1']) * int(least_zero_layer['2'])


with open('input', 'r') as file:
    lines = file.readlines()[0]
    print('Result: ' + str(find_pixels(lines)))
