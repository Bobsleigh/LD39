from ldLib.tools.ImageBox import ImageBox

__author__ = 'Bobsleigh'
import pygame
from app.settings import *

class LifeBar(pygame.sprite.Sprite):
    def __init__(self, sprite,x,y,width=32, height=5):
        super().__init__()
        self.width = width
        self.height = height
        self.sizeBorder = 2

        self.image = ImageBox().blackAndWhiteBorderBox(self.width, self.height, self.sizeBorder)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.sprite = sprite

    def update(self):
        maxHealth = self.sprite.maxHealth
        currentHealth = self.sprite.currentHealth

        dmg = maxHealth-currentHealth
        self.widthRed = int((self.width - 2 * self.sizeBorder) * (dmg) / maxHealth)
        if dmg > 0:
            dmgBar = pygame.Rect((self.width - 2 * self.sizeBorder) - self.widthRed + self.sizeBorder,
                                 self.sizeBorder,
                                 self.widthRed,
                                 self.height - 2 * self.sizeBorder)
            pygame.draw.rect(self.image, RED, dmgBar)