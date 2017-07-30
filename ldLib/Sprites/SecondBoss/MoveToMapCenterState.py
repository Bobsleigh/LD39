__author__ = 'Bobsleigh'

import pygame
from ldLib.Sprites.SecondBoss.EnemyState import EnemyState
from app.settings import *

class MoveToMapCenterState(EnemyState):
    def __init__(self):
        super().__init__()

    def update(self, sprite, mapData):
        if sprite.rect.centery < (mapData.tmxData.height * mapData.tmxData.tileheight)/2:
            sprite.updateSpeedDown()
        if sprite.rect.centery > (mapData.tmxData.height * mapData.tmxData.tileheight)/2:
            sprite.updateSpeedUp()
        if sprite.rect.centerx > (mapData.tmxData.width * mapData.tmxData.tilewidth)/2:
            sprite.updateSpeedLeft()
        if sprite.rect.centerx < (mapData.tmxData.width * mapData.tmxData.tilewidth)/2:
            sprite.updateSpeedRight()
    def enter(self, sprite):
        pass

    def exit(self, sprite):
        pass