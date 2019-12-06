#!/usr/bin/env python3

import re


def find_path_length(graph, node, counter):
    if node in graph:
        for n in graph[node]:
            counter += 1
            return find_path_length(graph, n, counter)
    else:
        return counter


def orbits(input):
    nodes = set()
    graph = {}
    for line in input:
        _, being_orbited, orbiter, _ = re.split('(.+)\\)(.+)', line)
        nodes.add(being_orbited)
        nodes.add(orbiter)
        if orbiter in graph:
            graph[orbiter].append(being_orbited)
        else:
            graph[orbiter] = [being_orbited]
    total = 0
    for node in nodes:
        path_size = find_path_length(graph, node, 0)
        total += path_size
    return total


with open('input', 'r') as file:
    lines = file.readlines()
    print('Result: ' + str(orbits(lines)))
