#!/usr/bin/env python3

from src.day9 import boost_program as boost


class Tile:

    def __init__(self, x, y, tile_id):
        self.x = int(x)
        self.y = int(y)
        self.tile_id = int(tile_id)


def paddle_move(paddle_x, ball_x):
    if paddle_x < ball_x:
        print('moving right')
        return 1
    elif paddle_x > ball_x:
        print('moving left')
        return -1
    else:
        print('staying')
        return 0


def print_tiles(output):
    x_coords = set()
    y_coords = set()
    w, h = 100, 100
    grid = [[0 for x in range(w)] for y in range(h)]
    tiles = []
    score_block = (-1, 0)
    score = 0
    paddle_x = 0
    ball_x = 0
    for tile_index in range(0, len(output), 3):
        tile = Tile(output[tile_index], output[tile_index+1], output[tile_index+2])
        #print('Tile: ', tile.x, ' ', tile.y, ' ', tile.tile_id)
        if tile.tile_id == 4:  # ball
            ball_x = tile.x
        elif tile.tile_id == 3:  # paddle
            paddle_x = tile.x
        if (tile.x, tile.y) == score_block:
            score = tile.tile_id
            continue
        x_coords.add(tile.x)
        y_coords.add(tile.y)
        try:
            grid[tile.x][tile.y] = tile.tile_id
        except:
            pass
        tiles.append(tile)
    print('Ball: ', ball_x, ' Paddle: ', paddle_x)
    x_range = (min(x_coords), max(x_coords))
    y_range = (min(y_coords), max(y_coords))
    print('x: ', x_range, ' y:', y_range)
    print('Score: ', str(score))
    for y in range(max(y_coords)+1):
        for x in range(max(x_coords)+1):
            tile_icon = ' '
            tile_id = grid[x][y]
            if tile_id == 1:  # wall
                tile_icon = '|'
            elif tile_id == 2:  # block
                tile_icon = '#'
            elif tile_id == 3:  # paddle
                tile_icon = '='
            elif tile_id == 4:  # ball
                tile_icon = '*'
            print(tile_icon, end='')
        print()
    # time.sleep(0.1)
    return paddle_move(paddle_x, ball_x)


if __name__ == '__main__':
    with open('input', 'r') as file:
        first_line = file.readlines()[0]
        input = list(map(int, first_line.split(",")))
        # set memory address 0 to 2 to play for free!
        input[0] = 2
        runner = boost.BoostProgram(input, [], print_tiles)
        output = runner.run()
        by_tile_id = {}
        for tile_index in range(0, len(output), 3):
            tile_id = output[tile_index+2]
            if str(tile_id) in by_tile_id:
                by_tile_id[str(tile_id)] += 1
            else:
                by_tile_id[str(tile_id)] = 1

        print('Result: ' + str(by_tile_id['2']))
