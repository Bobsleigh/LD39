from ldLib.tools.ImageBox import ImageBox

import pygame
from app.settings import *

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text,x,y,textColor=BLACK):
        super().__init__()
        font = pygame.font.Font(FONT_NAME, DIALOG_TEXT_SIZE)

        self.printedLine = font.render(text, True, textColor)
        self.image = self.printedLine
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y


    def update(self):
        pass
