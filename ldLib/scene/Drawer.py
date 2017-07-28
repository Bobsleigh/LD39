import pygame
import pyscroll

from app.settings import *

class Drawer:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.FPS = FPS

    def draw(self, screen, sprites, spritesHUD, spritesBackGround, player):

        spritesBackGround.draw(screen)

        if isinstance(sprites, pygame.sprite.Group):
            sprites.draw(screen)
        elif isinstance(sprites, pyscroll.PyscrollGroup) and player != None:
            sprites.center((player.rect.centerx, player.rect.centery - (HUD_HEIGHT / 2)))
            sprites.draw(screen)

        spritesHUD.draw(screen)
        pygame.display.flip()
        self.clock.tick(self.FPS)
