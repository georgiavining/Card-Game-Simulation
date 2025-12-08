from .deck import Deck
from .groups import is_valid_group
from .turn import TurnState

class Game:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.turn = TurnState(0)
        self.winner = None
        self.log = ["Game Started"]

        for i in range(4):
            for p in self.players:
                card = self.deck.draw_one()
                p.add_card(card)

    def current_player(self):
        return self.players[self.turn.player_index]

    def check_win(self):
        for p in self.players:
            if len(p.hand) == 0:
                self.winner = p

    def next_player(self):
        n = (self.turn.player_index + 1) % len(self.players)
        self.turn.reset(n)

    def add_log(self, message):
        self.log.append(message)
        if len(self.log) > 6: 
            self.log.pop(0)

    def draw_up_to_3(self, amount):
        player = self.current_player()

        if self.turn.used_draw_up_to_3:
            return "Already used this action"

        if amount < 1 or amount > 3:
            return "Can only draw 1 to 3 cards"

        if not player.can_take_more_cards(amount):
            return "Hand limit exceeded"

        drawn = self.deck.draw(amount)
        player.add_cards(drawn)

        self.turn.used_draw_up_to_3 = True
        self.check_win()
        self.add_log(f"{player.name} drew {len(drawn)} cards")
    
        return drawn

    def draw_up_to_3_step(self):
        player = self.current_player()

        if self.turn.used_draw_up_to_3:
            return "Already used this action"

        if len(self.turn.draw_up_to_3) >= 3:
            return "Cannot draw more than 3 cards"

        if not player.can_take_more_cards(1+len(self.turn.draw_up_to_3)):
            return "Hand limit exceeded"

        drawn = self.deck.draw_one()
        if drawn is None:
            return "Deck empty"

        self.turn.draw_up_to_3.append(drawn)
        
        return drawn
    
    def draw_up_to_3_done(self):
        player = self.current_player()

        for c in self.turn.draw_up_to_3:
            player.add_card(c)

        self.check_win()
        self.add_log(f"{player.name} drew {len(self.turn.draw_up_to_3)} cards")
        self.turn.used_draw_up_to_3 = True
        self.turn.draw_up_to_3 = []


    def steal_card(self, target_index):
        player = self.current_player()
        target = self.players[target_index]

        if player == target:
            return "Cannot steal from yourself"

        result = player.steal_from(target)

        self.turn.used_steal = True
        self.check_win()
        self.add_log(f"{player.name} stole a card from {target.name}")

        return result

    def draw_for_discard(self):
        if self.turn.used_draw_discard:
            return "Already used this action"

        player = self.current_player()
        drawn = self.deck.draw_one()

        if drawn is None:
            return "Deck empty"

        player.add_card(drawn)
        return drawn

    def discard_card(self, card_to_discard):
        player = self.current_player()
        if card_to_discard not in player.hand:
            return "Card not in hand"

        player.remove_card(card_to_discard)
        self.deck.add_and_shuffle([card_to_discard])

        self.turn.used_draw_discard = True
        self.check_win()
        self.add_log(f"{player.name} drew & discarded (Deck reshuffled)")


    def discard_group(self, cards):
        player = self.current_player()

        for c in cards:
            if c not in player.hand:
                return "Card not in hand"

        g = is_valid_group(cards)
        if g is None:
            return "Invalid group"

        for c in cards:
            player.remove_card(c)

        self.deck.add_and_shuffle(cards)
        self.check_win()
        self.add_log(f"{player.name} discarded {g} (Deck reshuffled)")
        return g

    def draw_and_discard(self, card_to_discard):
        res = self.draw_for_discard()
        if isinstance(res, str):
            return res
        
        res2 = self.discard_card(card_to_discard)
        return res2
