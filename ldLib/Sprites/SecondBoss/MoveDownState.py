__author__ = 'Bobsleigh'

import pygame
from ldLib.Sprites.SecondBoss.EnemyState import EnemyState
from app.settings import *

class MoveDownState(EnemyState):
    def __init__(self):
        super().__init__()

    def update(self, sprite, mapData):
        sprite.updateSpeedDown()

    def enter(self, sprite):
        pass

    def exit(self, sprite):
        pass