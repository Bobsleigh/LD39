import pygame
from app.settings import *

class ImageBox:
    def rectSurface(self, dimension, color=BLACK, border=0):
        if border >= 1:
            surface = pygame.Surface(dimension)
            surface.convert_alpha()
            surface.fill(BLACK)
            surface2 = pygame.Surface([dimension[0] - 2 * border, dimension[1] - 2 * border])
            surface2.fill(color)
            surface.blit(surface2, [border, border])
        else:
            surface = pygame.Surface(dimension)
            surface.fill(color)
        return surface