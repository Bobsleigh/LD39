__author__ = 'Bobsleigh'

import pygame
from app.settings import *

class PowerBar(pygame.sprite.Sprite):
    def __init__(self, max):
        super().__init__()
        self.image = pygame.Surface([16, 150])
        self.image.fill(COLOR_POWER_BAR_EMPTY)
        self.image.set_colorkey(COLOR_POWER_BAR_EMPTY)
        self.rect = self.image.get_rect()
        self.rect.x = 32
        self.rect.y = 10

        self.max = max
        self.current = 0
        self.isDisplayed = True

    def subtract(self, amount):
        self.current -= amount
        if self.current < 0:
            self.current = 0

    def add(self, amount):
        self.current += amount
        if self.current > self.max:
            self.current = self.max

    def set(self, value):
        self.current = value
        if self.current > self.max:
            self.current = self.max
        elif self.current < 0:
            self.current = 0
        self.update()

    def update(self):
        self.image.fill(COLOR_POWER_BAR_EMPTY)
        pwr = self.current
        if pwr > 0:
            pwrBar = pygame.Rect(0,150-150*(pwr)/self.max, 16, 150*(pwr)/self.max)
            pygame.draw.rect(self.image, COLOR_POWER_BAR, pwrBar)