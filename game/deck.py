import pygame
import random
from game.card import Card
from config import colours, numbers, deck_x, deck_y, card_width, card_height
from ui.visual_objects import ImageBasedObject

class Deck(ImageBasedObject):
    def __init__(self, x=deck_x, y=deck_y):
        super().__init__("assets/cards/back.png", x=x, y=y)
        self.image = pygame.transform.scale(self.image, (card_width, card_height))
        self.size = self.image.get_size()
        
        self.cards = [Card(col, num) for _ in range(2) for col in colours for num in numbers]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, players):
        for player in players:
            player.hand.add_to_hand(self.draw_from_deck(4))
        
    def draw_from_deck(self, num):
        return [self.cards.pop() for _ in range(min(num, len(self.cards)))]

    def add_to_deck(self, cards):
        self.cards.extend(cards)
        random.shuffle(self.cards)