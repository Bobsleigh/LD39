__author__ = 'Bobsleigh'

import pygame
import os

class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.imageOrig = pygame.image.load(os.path.join('img', 'lutecia-arrow.png'))
        self.image = self.imageOrig
        self.name = "target"

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speedx = 0
        self.speedy = 0

        self.isPhysicsApplied = False
        self.isGravityApplied = False
        self.isFrictionApplied = False
        self.isCollisionApplied = False

        self.powerx = 0
        self.powery = 0

    def dead(self):
        pass

    def spring(self):
        pass