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

    def blackAndWhiteBorderBox(self, width, height, border):
        surface = pygame.Surface((width,height),pygame.SRCALPHA)
        surface.convert_alpha()
        surface.blit(self.borderOnly(width,height,border,WHITE),[0,0])
        surface.blit(self.borderOnly(width-border*2, height-border*2, border), [border, border])

        return surface

    def borderOnly(self, width, height, border,color=BLACK):
        width = int(width)
        height = int(height)
        border = int(border)
        surface = pygame.Surface((width, height), pygame.SRCALPHA)

        surface.convert_alpha()

        # top line
        topLine = pygame.Surface([width, border])
        topLine.fill(color)
        surface.blit(topLine, [0, 0])

        # bottom line
        bottomLine = pygame.Surface([width, border])
        bottomLine.fill(color)
        surface.blit(bottomLine, [0, height - border])

        # left line
        leftLine = pygame.Surface([border, height])
        leftLine.fill(color)
        surface.blit(leftLine, [0, 0])

        # right line
        rightLine = pygame.Surface([border, height])
        rightLine.fill(color)
        surface.blit(rightLine, [width - border, 0])

        return surface