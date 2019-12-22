#!/usr/bin/env python3

from src.day22.part1 import Deck


def run_many_times(input):
    deck = Deck(119315717514047, input)
    # hhmm, this is not going to work!
    for _ in range(101741582076661):
        deck.shuffle_cards()
        print('After shuffling: ' + str(deck.cards))
    return deck


if __name__ == '__main__':
    with open('input', 'r') as file:
        input = file.readlines()
        deck = run_many_times(input)
        print('After shuffling: ' + str(deck.cards))
        print('Card found is: ' + str(deck.find_card(2020)))

