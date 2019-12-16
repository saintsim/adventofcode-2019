#!/usr/bin/env python3

from src.day13 import part2

import unittest


class TestBlocks(unittest.TestCase):
    def test_process_input(self):
        cases = [
            # 3 = paddle, 4 = ball
            ([1, 2, 3, 6, 5, 4], 1)
        ]

        for case in cases:
            self.assertEqual(case[1], part2.print_tiles(case[0]))
