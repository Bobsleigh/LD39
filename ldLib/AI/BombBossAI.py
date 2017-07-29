import math
from app.settings import *
from ldLib.tools.Counter import Counter
from ldLib.Sprites.BombBoss.Dash import Dash
from ldLib.Sprites.BombBoss.Boom import Boom
from ldLib.Sprites.BombBoss.Zap import Zap
import random


class BombBossAI:
    def __init__(self, sprite, mapData):
        self.sprite = sprite
        self.mapData = mapData

        self.counter = Counter()

    def update(self):
        self.counter.value += 1
        self.choose_state()

    def choose_state(self):
        if self.counter.value % 20 == 0:
            if self.counter.value > 1200:
                if random.randint(1, 4) == 1:
                    self.sprite.Dash()
                    self.counter.reset()
            if self.counter.value != 0:
                if self.counter.value % 300 == 0:
                    self.sprite.Boom()
                if self.counter.value > 480 and self.counter.value % 180 == 0:
                    self.sprite.Zap()

    def vectorNorm(self,x,y):
        result = math.sqrt(x**2+y**2)
        if result == 0:
            return 1

        return result