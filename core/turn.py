class TurnState:
    def __init__(self, player_index):
        self.player_index = player_index
        self.used_draw_up_to_3 = False
        self.used_steal = False
        self.used_draw_discard = False
        self.draw_up_to_3 = []

    def reset(self, next_player_index):
        self.player_index = next_player_index
        self.used_draw_up_to_3 = False
        self.used_steal = False
        self.used_draw_discard = False

    