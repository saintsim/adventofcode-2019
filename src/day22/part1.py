#!/usr/bin/env python3

import re

'''
cards in the deck numbered 0 through 10006
they're still in factory order, with 0 on the top, then 1, then 2, and so on

[1] deal into new stack
    Reverse it, e.g. 0;1;2;3;4 -> 4;3;2;1;0

[2] cut N
    take the top N cards off the top of the deck and
    move them as a single unit to the bottom of the deck, retaining their order
    e.g. if N = 2 and deck is 0;1;2;3;4 -> 2;3;4;0;1
    Also works if N is negative, e.g. -2 and deck is 0;1;2;3;4 -> 3;4;0;1;2

[3] deal with increment N

    start by clearing enough space on your table to lay out all of the cards individually in a long line.
    Deal the top card into the leftmost position.
    Then, move N positions to the right and deal the next card there.
    e.g if N = 2 and deck is
        0;1;2;3;4 ->
        0 1 2 3 4
        0 _ 1 _ 2
        0 3 1 4 2

'''

DECK = []


def create_deck(number_of_cards, default_value=''):
    new_deck = []
    for i in range(number_of_cards):
        if default_value != '':
            new_deck.append(default_value)
        else:
            new_deck.append(i)
    return new_deck


def apply_rule(rule):
    global DECK
    if rule.startswith('deal into new stack'):
        DECK.reverse()
    elif rule.startswith('cut'):
        _, n, _ = re.split('cut (.+)', rule)
        n = int(n)
        if n > 0:
            DECK = DECK[n:] + DECK[0:n]
        else:
            DECK = DECK[len(DECK) - abs(n):] + DECK[0:len(DECK)-abs(n)]
        pass
    elif rule.startswith('deal with increment'):
        _, n, _ = re.split('deal with increment (.+)', rule)
        n = int(n)
        new_deck = create_deck(len(DECK), 'NULL')
        deck_index = 0
        for idx in range(len(DECK)):
            if deck_index < len(DECK):
                new_deck[deck_index] = DECK[idx]
            else:
                new_deck[(deck_index%len(DECK))] = DECK[idx]
                deck_index = (deck_index%len(DECK))
            deck_index += n
        DECK = list(new_deck)
    else:
        Exception('Invalid rule')


def shuffle_cards(shuffle_rules, number_of_cards):
    global DECK
    DECK = create_deck(number_of_cards)
    for rule in shuffle_rules:
        apply_rule(rule)
    return str(DECK)


def find_card(card_to_find):
    for idx, el in enumerate(DECK):
        if el == card_to_find:
            return idx


if __name__ == '__main__':
    with open('input', 'r') as file:
        input = file.readlines()
        print('After shuffling: ' + str(shuffle_cards(input, 10007)))
        print('Card found is: ' + str(find_card(2019)))
