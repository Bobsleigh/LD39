import math
import random
from app.settings import *
from ldLib.tools.Counter import Counter
from ldLib.tools.Cooldown import Cooldown
import random


class BombBossAI:
    def __init__(self, sprite, mapData):
        self.sprite = sprite
        self.mapData = mapData

        self.counter = Counter()
        self.cooldown = Cooldown(180)
        self.difficulty = 0

    def update(self):
        self.cooldown.update()
        if self.cooldown.isZero:
            self.counter.value += 1
        self.update_difficulty()
        self.choose_state()

    def update_difficulty(self):
        if (self.sprite.currentHealth/self.sprite.maxHealth) < 0.3:
            self.difficulty = 3
        elif (self.sprite.currentHealth/self.sprite.maxHealth) < 0.6:
            self.difficulty = 2

    def choose_state(self):
        if self.difficulty != 3 and self.cooldown.isZero:
            if self.counter.value % 20 == 0:
                if self.counter.value > 2400:
                    self.difficulty = max(1, self.difficulty)
                    self.counter.reset()
                if self.counter.value != 0:
                    if self.counter.value % 600 == 0:
                        if self.difficulty == 2:
                            self.sprite.prettyZap(3)
                            self.counter.value += 1
                            self.cooldown.start()
                    if self.counter.value % 300 == 0:
                        self.sprite.Boom()
                    if self.counter.value % 400 == 0 and self.difficulty == 0:
                        self.sprite.smallDash()
                    if self.difficulty != 0 and self.counter.value % 80 == 0:
                        self.sprite.Zap()
                    if self.counter.value % 140 == 0:
                        if self.difficulty == 0:
                            self.sprite.Zap()
                        else:
                            self.sprite.Dash()

        else:
            if self.counter.value % 200 == 0:
                pattern = random.randint(1, 2)
                self.sprite.prettyZap(pattern)
            if self.counter.value % 300 == 0:
                self.sprite.Dash()
            if self.counter.value % 400 == 0:
                self.sprite.boomOnPlate()

    def vectorNorm(self,x,y):
        result = math.sqrt(x**2+y**2)
        if result == 0:
            return 1

        return result