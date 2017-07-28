from app.settings import *
import pygame
import os

class ScoreDisplay(pygame.sprite.Sprite):
    def __init__(self,fontSize=12):
        super().__init__()

        self.image=pygame.image.load(os.path.join('img', 'enemybob.png'))
        self.rect = self.image.get_rect()
        self.hudFont = pygame.font.SysFont(MENU_FONT, fontSize)
        self.number = self.hudFont.render('position: ', True, HUD_FONT_COLOR)