import random

class Player:
    def __init__(self, name, is_human=True, ai_type=None):
        self.name = name
        self.is_human = is_human
        self.ai_type = ai_type
        self.hand = []

    def hand_size(self):
        return len(self.hand)

    def add_card(self, card):
        self.hand.append(card)

    def add_cards(self, cards):
        for c in cards:
            self.hand.append(c)

    def remove_card(self, card):
        if card in self.hand:
            self.hand.remove(card)

    def can_take_more_cards(self, amount):
        return len(self.hand) + amount <= 20
    
    def steal_from(self, target_player):
        if len(target_player.hand) == 0:
            return "Target has no cards"
        if not self.can_take_more_cards(1):
            return "Hand limit exceeded"

        card = random.choice(target_player.hand)
        target_player.remove_card(card)
        self.add_card(card)
        return card


