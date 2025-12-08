import random
from .card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.create_full_deck()
        self.shuffle()
        

    def create_full_deck(self):
        colours = ["red", "green", "yellow", "blue", "black"]
        for colour in colours:
            for number in range(1, 10):

                self.cards.append(Card(colour, number))
                self.cards.append(Card(colour, number))

    def shuffle(self):

        random.shuffle(self.cards)


    def draw(self, n):

        drawn = []

        for _ in range(min(n, len(self.cards))):
            drawn.append(self.cards.pop())
        return drawn

    def draw_one(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None

    def add_and_shuffle(self, cards):

        self.cards.extend(cards)
        self.shuffle()
