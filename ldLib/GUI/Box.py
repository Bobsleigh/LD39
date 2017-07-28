import pygame
import os
from app.settings import *


class Box(pygame.sprite.Sprite):
    def __init__(self,pos, size):
        super().__init__()

        x = size[0]
        y = size[1]

        TILEX = 32
        TILEY = 32
        upLeft = pygame.image.load(os.path.join('img', 'GUI', "GreyUpLeft.bmp"))
        upMid = pygame.image.load(os.path.join('img', 'GUI', "GreyUpMid.bmp"))
        upRight = pygame.image.load(os.path.join('img', 'GUI', "GreyUpRight.bmp"))
        midLeft = pygame.image.load(os.path.join('img', 'GUI', "GreyMidLeft.bmp"))
        center = pygame.image.load(os.path.join('img', 'GUI', "GreyCenter.bmp"))
        midRight = pygame.image.load(os.path.join('img', 'GUI', "GreyMidRight.bmp"))
        downLeft = pygame.image.load(os.path.join('img', 'GUI', "GreyDownLeft.bmp"))
        downMid = pygame.image.load(os.path.join('img', 'GUI', "GreyDownMid.bmp"))
        downRight = pygame.image.load(os.path.join('img', 'GUI', "GreyDownRight.bmp"))

        self.box = pygame.Surface((x, y))

        self.box.blit(upLeft, (0,0))
        for i in range((x//TILEX)-1):
            self.box.blit(upMid, (TILEX+i*TILEX,0))
        self.box.blit(upRight, (x-TILEX,0))

        for j in range(1, y//TILEY):
            self.box.blit(midLeft, (0,j*TILEY))
            for i in range((x//TILEX)-1):
                self.box.blit(center, (TILEX+i*TILEX,j*TILEY))
            self.box.blit(midRight, (x-TILEX,j*TILEY))

        self.box.blit(downLeft, (0,y-TILEY))
        for i in range((x//TILEX)-1):
            self.box.blit(downMid, (TILEX+i*TILEX,y-TILEY))
        self.box.blit(downRight, (x-TILEX,y-TILEY))

        self.image = self.box
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]