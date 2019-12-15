#!/usr/bin/env python3

from src.day9 import boost_program as boost


if __name__ == '__main__':
    with open('input', 'r') as file:
        first_line = file.readlines()[0]
        runner = boost.BoostProgram(list(map(int, first_line.split(","))), [])
        output = runner.run()
        by_tile_id = {}
        for tile_index in range(0, len(output), 3):
            tile_id = output[tile_index+2]
            if str(tile_id) in by_tile_id:
                by_tile_id[str(tile_id)] += 1
            else:
                by_tile_id[str(tile_id)] = 1
        print('Result: ' + str(by_tile_id['2']))
