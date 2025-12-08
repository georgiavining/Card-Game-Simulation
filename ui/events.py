import pygame

def get_clicked_opponent(mx, my, num_players):
    w = 150
    h = 50
    y = 50

    x1 = 50
    r1 = pygame.Rect(x1, y, w, h)
    if num_players > 1 and r1.collidepoint(mx, my):
        return 1

    if num_players == 3:
        x2 = 250
        r2 = pygame.Rect(x2, y, w, h)
        if r2.collidepoint(mx, my):
            return 2

    return None