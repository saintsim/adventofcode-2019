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


class Deck:

    def __init__(self, number_of_cards, rules):
        self.cards = Deck.create_deck(number_of_cards)
        self.shuffle_rules = rules

    @staticmethod
    def create_deck(number_of_cards, default_value=''):
        new_deck = []
        for i in range(number_of_cards):
            if default_value != '':
                new_deck.append(default_value)
            else:
                new_deck.append(i)
        return new_deck

    def apply_rule(self, rule):
        if rule.startswith('deal into new stack'):
            self.cards.reverse()
        elif rule.startswith('cut'):
            _, n, _ = re.split('cut (.+)', rule)
            n = int(n)
            if n > 0:
                self.cards = self.cards[n:] + self.cards[0:n]
            else:
                self.cards = self.cards[len(self.cards) - abs(n):] + self.cards[0:len(self.cards)-abs(n)]
            pass
        elif rule.startswith('deal with increment'):
            _, n, _ = re.split('deal with increment (.+)', rule)
            n = int(n)
            new_deck = Deck.create_deck(len(self.cards), 'NULL')
            deck_index = 0
            for idx in range(len(self.cards)):
                if deck_index < len(self.cards):
                    new_deck[deck_index] = self.cards[idx]
                else:
                    new_deck[(deck_index%len(self.cards))] = self.cards[idx]
                    deck_index = (deck_index%len(self.cards))
                deck_index += n
            self.cards = list(new_deck)
        else:
            Exception('Invalid rule')

    def shuffle_cards(self):
        for rule in self.shuffle_rules:
            self.apply_rule(rule)
        return str(self.cards)

    def find_card(self, card_to_find):
        for idx, el in enumerate(self.cards):
            if el == card_to_find:
                return idx


if __name__ == '__main__':
    with open('input', 'r') as file:
        input = file.readlines()
        deck = Deck(10007, input)
        print('After shuffling: ' + str(deck.shuffle_cards()))
        print('Card found is: ' + str(deck.find_card(2019)))
