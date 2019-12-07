#!/usr/bin/env python3

from src.day5 import part1

import unittest


class TestDiagnosticProgram(unittest.TestCase):
    def test_process_input(self):
        cases = [
            ([1002, 4, 3, 4, 33], 1002)
        ]

        for case in cases:
            self.assertEqual(case[1], part1.diagnostic_program(case[0]))
