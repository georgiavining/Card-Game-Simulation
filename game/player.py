from game.hand import Hand
import random
from game.deck import Deck
from game.rules import Rules
from abc import ABC, abstractmethod


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

class ComputerPlayer(Player):
    def __init__(self, name, strategy= None): 
        super().__init__(name)
        self.strategy = strategy or RandomStrategy()

    def draw_cards(self,state, deck):
        number_to_draw = self.strategy.select_draw(self.hand, state) 
        if number_to_draw != 0:
            drawn_cards = deck.draw_from_deck(number_to_draw)
            if drawn_cards:
                self.hand.add_to_hand(drawn_cards)
            
    def take_card(self, state):
        result = self.strategy.select_take(self, self.hand, state)
        if result is not None:
            card, target_player = result
            target_player.hand.cards.remove(card)
            self.hand.add_to_hand([card])

    def draw_and_discard(self, state, deck):
        if self.strategy.select_draw_and_discard(self.hand, state) == True:
            drawn_card = deck.draw_from_deck(1)
            if drawn_card:
                self.hand.add_to_hand(drawn_card)
                discard_card = self.strategy.select_discard(self.hand, state)  
                self.hand.cards.remove(discard_card)
                deck.add_to_deck(discard_card)

    def discard_groups(self,state, deck):
        discarded = []
        discard_groups = self.strategy.select_discard_groups(self.hand, state)
        if discard_groups:
            for group in discard_groups:  
                self.hand.remove_group(group)
                discarded.append(group)
            deck.add_to_deck(discarded)

    def take_turn(self, state, deck):
        actions = self.strategy.take_turn(self, state, deck)
        for action in actions:
            action()  

    
class Strategy(ABC):
    
    @abstractmethod
    def select_draw(self, hand, state):
        """Returns number between 0 and 3 regarding how many cards to draw"""
        pass

    @abstractmethod
    def select_take(self, hand, state):
        """
        Returns a tuple (card, target_player) if bot wants to take a card 
        from another player, or None if no action
        """
        pass
    
    @abstractmethod
    def select_draw_and_discard(self, hand, state):
        """Returns True if bot wants to draw a card and then discard a card"""
        pass

    @abstractmethod
    def select_discard(self, hand, state):
        """Returns the card to discard from hand"""
        pass

    @abstractmethod
    def select_discard_groups(self, hand, state):
        """Returns valid group/s to discard """
        pass

    @abstractmethod
    def take_turn(self, player,state, deck):
        """Returns a list of callables representing the actions to execute"""
        pass



class RandomStrategy(Strategy):
    def select_draw(self, hand, state):
        if len(hand) <= 17:
            return random.randint(0,3)
        elif len(hand) == 18:
            return random.randint(0,2)
        elif len(hand) == 19:
            return random.randint(0,1)
        else:
            return 0

    def select_take(self, player, hand, state):
        if len(hand) <= 19:
            pos_targets = [p for p in state.players if p.hand.cards and p != player]
            if pos_targets:
                target_player = random.choice(pos_targets)
                card = random.choice(target_player.hand.cards)
                return card, target_player
        return None

    def select_draw_and_discard(self, hand, state):
        return random.choice([True, False])

    def select_discard(self, hand, state):
        if hand.cards:
            return random.choice(hand.cards)
        return None
    
    def select_discard_groups(self, hand, state):
        valid_groups = Rules.find_valid_groups(hand)
        discard_groups = []
        used_cards = set()
        
        if valid_groups:
            for group in valid_groups:

                if any(id(card) in used_cards for card in group):
                    continue

                discard_groups.append(group)

                for card in group:
                    used_cards.add(id(card))

            random.shuffle(discard_groups)
            num_to_discard = random.randint(1, len(discard_groups))
            return discard_groups[:num_to_discard]
        return None
    
    def take_turn(self, player, state, deck):
        once_actions = [
            lambda: player.draw_cards(state,deck),
            lambda: player.take_card(state),
            lambda: player.draw_and_discard(state, deck)
        ]

        repeat_actions = [
            lambda: player.discard_groups(state, deck)
        ]

        random.shuffle(once_actions)

        return once_actions 
    

#class BetterStrategy(Strategy):


