#!/usr/bin/env python3

from src.day4 import part2

import unittest


class TestPassword(unittest.TestCase):
    def test_process_input(self):
        cases = [
            (112233, 112233, 1),
            (123444, 123444, 0),
            (111122, 111122, 1)
        ]

        for case in cases:
            self.assertEqual(case[2], part2.password_cracker(case[0], case[1]))
