from ldLib.tools.ImageBox import ImageBox

__author__ = 'Bobsleigh'
import pygame
from app.settings import *

class LifeBar(pygame.sprite.Sprite):
    def __init__(self, sprite,x,y,width=32, height=5, lifeColor = LIFE_BAR_COLOR):
        super().__init__()
        self.barColor = lifeColor
        self.width = width
        self.height = height
        self.sizeBorder = 4

        self.image = ImageBox().blackAndWhiteBorderBox(self.width, self.height, self.sizeBorder)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.sprite = sprite

    def update(self):
        self.image = ImageBox().blackAndWhiteBorderBox(self.width, self.height, self.sizeBorder)

        maxHealth = self.sprite.maxHealth
        currentHealth = self.sprite.currentHealth

        self.widthLife = int((self.width - 4 * self.sizeBorder) * currentHealth / maxHealth)
        if currentHealth > 0:
            dmgBar = pygame.Rect(2 * self.sizeBorder,
                                 2 * self.sizeBorder,
                                 self.widthLife,
                                 self.height - 4 * self.sizeBorder)
            pygame.draw.rect(self.image, self.barColor, dmgBar)