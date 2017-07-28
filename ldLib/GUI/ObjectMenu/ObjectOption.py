__author__ = 'Bobsleigh'

import pygame
from app.settings import *

from app.tools.messageBox.textLine import TextLine


#For a very short message only

class ObjectOption(pygame.sprite.Sprite):
    def __init__(self, name, fontSize=20):
        super().__init__()

        self.optFont = pygame.font.SysFont(MENU_FONT, fontSize)
        self.name = name
        self.printedName = self.optFont.render(self.name, True, MENU_FONT_COLOR)
        self.textPos = [0,0] #Par rapport au bouton

        self.image = pygame.Surface([1, 1])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.button = pygame.Rect(0,0,0,0)

        self.isSelected = False
        # self.soundSelect = pygame.mixer.Sound('music_pcm/menu_select.wav')
        # self.soundSelect.set_volume(.3)
        # self.soundChange = pygame.mixer.Sound('music_pcm/menu_change.wav')
        # self.soundChange.set_volume(.3)

        #Color
        self.color1 = COLOR_MENU_1
        self.color2 = COLOR_MENU_2

    def update(self):
        self.printedName = self.optFont.render(self.name, True, MENU_FONT_COLOR)

        # self.image.fill(self.color2)
        self.image.fill(self.color1)
        self.image.blit(self.printedName,self.textPos)

    def select(self):
        self.isSelected = True
        # self.soundChange.play(0)

    def selectQuit(self):
        # self.soundSelect.play(0)
        pass

    def deselect(self):
        self.isSelected = False

    def doOption(self):
        # self.soundSelect.play(0)
        self.method()