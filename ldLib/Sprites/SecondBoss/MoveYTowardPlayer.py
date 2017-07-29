__author__ = 'Bobsleigh'

import pygame
from ldLib.Sprites.SecondBoss.EnemyState import EnemyState
from app.settings import *

class MoveYTowardPlayer(EnemyState):
    def __init__(self, mapData):
        super().__init__()
        self.mapData = mapData
        self.direction = UP

    def update(self, sprite, mapData):
        if self.direction == UP:
            sprite.updateSpeedUp()
        if self.direction == DOWN:
            sprite.updateSpeedDown()

    def enter(self, ai):
        if self.mapData.player.rect.y < ai.sprite.rect.y:
            self.direction = UP
        else:
            self.direction = DOWN

    def exit(self, sprite):
        pass