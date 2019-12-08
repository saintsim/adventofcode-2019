#!/usr/bin/env python3

from termcolor import colored


def parse_pixels(pixels, area):
    pixel_index = 0
    layers = []
    while pixel_index < len(pixels):
        layer = []
        while len(layer) < area:
            layer.append(pixels[pixel_index])
            pixel_index += 1
        layers.append(layer)
    return layers


def decode_image(layers, size_x):
    # 0 is black, 1 is white, and 2 is transparent.
    final_image = []
    index = 0
    depth = len(layers)
    for pixel in layers[0]:
        pixel_colour = ''
        for depth_index in range(0,depth):
            if layers[depth_index][index] == '0':
                pixel_colour = '0'
                break
            if layers[depth_index][index] == '1':
                pixel_colour = '1'
                break
        if pixel_colour == '':
            pass
        final_image.append(pixel_colour)
        index += 1
    index = 0
    for pixel in final_image:
        if pixel == '0':
            print(colored('X', 'white'), end='')
        else:
            print(colored('X', 'red'), end='')
        index += 1
        if index % size_x == 0:
            print('')


def make_image(pixels):
    size_x = 25
    size_y = 6
    area = size_x * size_y
    layers = parse_pixels(pixels, area)
    decode_image(layers, size_x)


with open('input', 'r') as file:
    lines = file.readlines()[0]
    print('Result: ' + str(make_image(lines)))
