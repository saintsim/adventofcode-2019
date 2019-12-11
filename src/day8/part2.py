#!/usr/bin/env python3

from termcolor import colored


def parse_pixels(pixels, number_of_pixels_per_layer):
    pixel_index = 0
    layers = []
    while pixel_index < len(pixels):
        layer = []
        while len(layer) < number_of_pixels_per_layer:
            layer.append(pixels[pixel_index])
            pixel_index += 1
        layers.append(layer)
    return layers


def decode_image(layers, number_of_pixels_per_layer):
    # 0 is black, 1 is white, and 2 is transparent.
    final_image = []
    depth = len(layers)
    # figure out the final colour for each pixel in the final image
    for pixel_index in range(number_of_pixels_per_layer):
        pixel_colour = ''
        # go over each layer to find this out, stop when we have white or black
        for depth_index in range(depth):
            if layers[depth_index][pixel_index] == '0':
                pixel_colour = '0'
                break
            elif layers[depth_index][pixel_index] == '1':
                pixel_colour = '1'
                break
        if pixel_colour == '':
            Exception('Unexpected colour')
        # add the pixel colour we found to the final image
        final_image.append(pixel_colour)
    return final_image


def print_image(image, size_x):
    index = 0
    for pixel in image:
        if pixel == '1':  # white is the foreground
            print(colored('%', 'red'), end='')
        else:  # black is the background
            print(' ', end='')
        index += 1
        if index % size_x == 0:
            print('')


def make_image(pixels, size_x, size_y):
    number_of_pixels_per_layer = size_x * size_y
    layers = parse_pixels(pixels, number_of_pixels_per_layer)
    final_image = decode_image(layers, number_of_pixels_per_layer)
    print_image(final_image, size_x)


with open('input', 'r') as file:
    input_line = file.readlines()[0]
    make_image(input_line, 25, 6)
