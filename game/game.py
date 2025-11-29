from __future__ import annotations
from game.deck import Deck
from game.player import Player, ComputerPlayer
from game.rules import Rules
from game.turn_manager import TurnManager
from config import screen_height,screen_width
from typing import List, Optional
from game.state import GameState
from game.card import Card
import random

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player("You"), ComputerPlayer("Computer")]
        self.status: str = "not_started"  # "not_started" | "running" | "finished"
        self.state = GameState(self.players)
        self.rules = Rules()
        self.turn_manager = TurnManager(self,self.players,self.deck)
        self.winner = None

    def start(self):
        """
        Start the game.

        - Shuffles the deck.
        - Deals 4 cards to each player.
        - Sets state to "running".
        """
        if self.status != "not_started":
            raise RuntimeError("Game already started.")
        
        self.deck.shuffle()
        self.deck.deal(self.players)
        self.winner = None
        self.status = "running"
     

    def update(self):
        self.turn_manager.run_turn()


    def _action_draw_up_to_three(self, player: "Player"):

        """draw up to 3 cards from the deck."""

        if self.turn_manager.draws_this_turn >= 3:
            return False  

        drawn_card = self.deck.draw_from_deck(1)
        if drawn_card and len(player.hand) + len(player.hidden_draw_pile) <= 19:
            player.hidden_draw_pile.append(drawn_card[0])  # hide drawn cards
            self.turn_manager.draws_this_turn += 1
            return True
        return False

    def reveal_drawn_cards(self, player: "Player"):
        if player.hidden_draw_pile:
            player.hand.add_to_hand(player.hidden_draw_pile)
            player.hidden_draw_pile = []
            self.turn_manager.draws_this_turn = 0

    def _action_steal_random(self, player: "Player",target: Optional["Player"]):

        """take a random card from another player."""

        
        if target is None or target is player:
            return False
        
        if not target.hand:
            return False
        
        if len(player.hand) == 20:
            return False
        
        card = random.choice(target.hand.cards)
        player.hand.append(card)
        target.hand.remove(card)

        return True

    def _action_draw_and_discard(self, player: "Player", discard_card: Optional["Card"]):
        """draw one card, then discard one card."""

        if not self.deck.cards:
            return False
        

        new_card = self.deck.draw_from_deck(1)
        if new_card is None:
            return False
        

        player.hand.append(new_card)

        # the card we just drew.
        if discard_card is None:
            discard_card = new_card

        if discard_card not in player.hand:
            # Invalid discard choice – undo the draw
            player.hand.remove(new_card)

            self.deck.add_to_deck([new_card])
            return False

        # Remove from hand and reshuffle into deck
        player.hand.remove(discard_card)

        return True

    def _action_discard_group(self, player: "Player", group):
        """discard a valid group of cards."""
        if not group:
            return False

        player=self.turn_manager.get_current_player()
        # Make sure all cards really belong to this player
        if any(card not in player.hand for card in group):
            return False

        if not self.rules.is_valid_group(group):
            return False
        
        # Remove cards from the player's hand
        player.hand.remove(group)
        self.deck.add_to_deck(group)

        return True

    def end_turn(self):
        self.turn_manager.current_turn_complete = True
        self.turn_manager.draws_this_turn = 0

    def play_for_me(self) :
        """""
        This method makes the current player
        play their turn using a computer strategy.
        """
        player = self.turn_manager.get_current_player()
        player.take_turn(self.state, self.deck)

        if self.rules.check_winner(self):
            return

        self.end_turn()


    def perform_action(self, player: "Player", action: str, **kwargs) :
        """
        Perform one of the four actions defined in the rules.

        Args:
            player: the player performing the action
            action: name of the action, for example:
                    "draw_up_to_three", "steal_random",
                    "draw_and_discard", "discard_group"
            **kwargs: extra data needed for the action (e.g. which
                      other player to steal from, which group to discard).

        Returns:
            True if the action was valid and performed successfully,
            False if the action was not allowed or invalid.

        """
        if self.status != "running":
            return False

        if isinstance(player, ComputerPlayer):
            return False

        if action == "draw_up_to_three":
            return self._action_draw_up_to_three(player)
        elif action == "steal_random":
            return self._action_steal_random(player, kwargs.get("target"))
        elif action == "draw_and_discard":
            return self._action_draw_and_discard(player, kwargs.get("discard_card"))
        elif action == "discard_group":
            return self._action_discard_group(player,kwargs.get("group"))
        elif action == "end_turn":
            return self.end_turn()
        elif action == "reveal_drawn_cards":
            return self.reveal_drawn_cards(player)
        elif action == "play_for_me":
            return self.play_for_me()
        else:
            # Unknown action
            return False
 
    
