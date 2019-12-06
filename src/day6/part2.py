#!/usr/bin/env python3

import re

graph_to_home = {}
graph_going_away = {}


def find_path_length(path_from, path_to):
    explored = []
    queue = [[path_from]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = []
            if node in graph_to_home:
                neighbours += graph_to_home[node]
            if node in graph_going_away:
                neighbours += graph_going_away[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == path_to:
                    return new_path

            # mark node as explored
            explored.append(node)
    return ''


def orbits(input):
    nodes = set()
    for line in input:
        _, being_orbited, orbiter, _ = re.split('(.+)\\)(.+)', line)
        nodes.add(being_orbited)
        nodes.add(orbiter)
        if orbiter in graph_to_home:
            graph_to_home[orbiter].append(being_orbited)
        else:
            graph_to_home[orbiter] = [being_orbited]
        if being_orbited in graph_going_away:
            graph_going_away[being_orbited].append(orbiter)
        else:
            graph_going_away[being_orbited] = [orbiter]
    print(graph_to_home)
    print(graph_going_away)
    path_from = graph_to_home['YOU'][0]
    path_to = graph_to_home['SAN'][0]
    path = find_path_length(path_from, path_to)
    return len(path)-1


with open('input', 'r') as file:
    lines = file.readlines()
    print('Result: ' + str(orbits(lines)))
