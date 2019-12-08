#!/usr/bin/env python3

import collections


def find_pixels(pixels, size_x, size_y):
    number_of_pixels_per_layer = size_x * size_y
    zero_count = number_of_pixels_per_layer  # this is the max number of 0's possible
    least_zero_layer = []
    pixel_index = 0
    while pixel_index < len(pixels):
        layer = []
        while len(layer) < number_of_pixels_per_layer:
            layer.append(pixels[pixel_index])
            pixel_index += 1
        counter = collections.Counter(layer)
        if counter['0'] < zero_count:
            least_zero_layer = counter
            zero_count = counter['0']
    return int(least_zero_layer['1']) * int(least_zero_layer['2'])


with open('input', 'r') as file:
    input_line = file.readlines()[0]
    print('Result: ' + str(find_pixels(input_line, 25, 6)))
