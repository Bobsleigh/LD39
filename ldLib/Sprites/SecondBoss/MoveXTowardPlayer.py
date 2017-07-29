__author__ = 'Bobsleigh'

import pygame
from ldLib.Sprites.SecondBoss.EnemyState import EnemyState
from app.settings import *

class MoveXTowardPlayer(EnemyState):
    def __init__(self, mapData):
        super().__init__()
        self.mapData = mapData
        self.direction = LEFT

    def update(self, sprite, mapData):
        if self.direction == LEFT:
            sprite.updateSpeedLeft()
        if self.direction == RIGHT:
            sprite.updateSpeedRight()

    def enter(self, ai):
        if self.mapData.player.rect.x < ai.sprite.rect.x:
            self.direction = LEFT
        else:
            self.direction = RIGHT

    def exit(self, sprite):
        pass