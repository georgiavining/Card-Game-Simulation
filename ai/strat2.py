import random
from core.groups import is_valid_group

def find_first_group(hand):

    n = len(hand)
    for i in range(n):

        for j in range(i + 1, n):
            for k in range(j + 1, n):
                cards = [hand[i], hand[j], hand[k]]
                if is_valid_group(cards) is not None:
                    return cards
                

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    cards = [hand[i], hand[j], hand[k], hand[l]]
                    
                    if is_valid_group(cards) is not None:
                        return cards
    return None

def strat2(game, max_actions=10):
    if game.winner is not None:
        return

    actions_taken = 0

    while actions_taken < max_actions and game.winner is None:
        player = game.current_player()
        can_draw_more = player.can_take_more_cards(1)
        group_cards = find_first_group(player.hand)

        possible = []

        if not game.turn.used_draw_up_to_3 and can_draw_more and len(game.deck.cards) > 0:
            possible.append("draw_up_to_3")

        steal_targets = []
        if not game.turn.used_steal and can_draw_more:
            for i, p in enumerate(game.players):
                if i != game.turn.player_index and len(p.hand) > 0:
                    steal_targets.append(i)
            if len(steal_targets) > 0:
                possible.append("steal")

        if not game.turn.used_draw_discard and len(game.deck.cards) > 0 and len(player.hand) > 0:
            possible.append("draw_discard")

        if group_cards is not None:
            possible.append("discard_group")

        possible.append("pass")

        if possible == ["pass"]:
            break

        action = random.choice(possible)

        if action == "draw_up_to_3":
            amount = random.randint(1, 3)
            game.draw_up_to_3(amount)

        elif action == "steal":
            target_index = random.choice(steal_targets)
            if len(game.players[target_index].hand) > 1:
                game.steal_card(target_index)

        elif action == "draw_discard":
            discard_card = random.choice(player.hand)
            game.draw_and_discard(discard_card)

        elif action == "discard_group":
            if group_cards is not None:
                game.discard_group(group_cards)

        elif action == "pass":
            break

        actions_taken += 1

        if game.winner is not None:
            break
    
    did_act = (actions_taken > 0)

    game.next_player()
    return did_act



