__author__ = 'Bobsleigh'

import pygame, random
from ldLib.Sprites.SecondBoss.EnemyState import EnemyState
from ldLib.tools.Counter import Counter
from app.settings import *

class MoveRandomState(EnemyState):
    def __init__(self, framesBeforeChangingDirection, variance=0):
        super().__init__()
        self.counter = Counter()
        self.framesBeforeChangingDirection = framesBeforeChangingDirection
        self.variance = variance
        self.counterCap = self.framesBeforeChangingDirection + random.randint(-self.variance, self.variance)
        self.direction = 0

    def update(self, sprite, mapData):
        if self.counter.value >= self.counterCap:
            self.direction = random.randint(0,3)
            self.counter.reset()
            self.counterCap = self.framesBeforeChangingDirection + random.randint(-self.variance, self.variance)
        else:
            self.counter.value += 1

        if self.direction == 0:
            sprite.updateSpeedDown()
        elif self.direction == 1:
            sprite.updateSpeedUp()
        elif self.direction == 2:
            sprite.updateSpeedLeft()
        elif self.direction == 3:
            sprite.updateSpeedRight()

    def enter(self, sprite):
        pass

    def exit(self, sprite):
        pass