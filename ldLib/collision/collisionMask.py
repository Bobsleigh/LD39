__author__ = 'Bobsleigh'

import pygame


class CollisionMask(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.rect = pygame.Rect(x, y, width, height)
