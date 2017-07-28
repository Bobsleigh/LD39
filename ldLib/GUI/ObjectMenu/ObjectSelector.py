__author__ = 'Bobsleigh'

import pygame
from app.settings import *

class ObjectSelector(pygame.sprite.Sprite):
    def __init__(self,num):
        #Default position
        self.selectedIndex = 0
        self.maxOpt = num

        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()
        self.image.fill(COLOR_MENU_SELECTOR)
        self.rect.x = 0
        self.rect.y = 0

    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveUp(self):
        if self.selectedIndex > 0:
            self.selectedIndex += -1
        # Skip Wrap Around
        # elif self.selectedIndex == 0:
        #     self.selectedIndex = self.maxOpt-1

    def moveDown(self):
        if self.selectedIndex < self.maxOpt-1:
            self.selectedIndex += 1
        # Skip Wrap Around
        # elif self.selectedIndex == self.maxOpt-1:
        #     self.selectedIndex = 0