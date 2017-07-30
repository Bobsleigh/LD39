import math
import random
from app.settings import *
from ldLib.tools.Counter import Counter
from ldLib.tools.Cooldown import Cooldown
import random


class GuardBossAI:
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
        if self.difficulty != 3:
            if self.counter.value % 20 == 0:
                if self.counter.value > 2400:
                    self.difficulty = max(1, self.difficulty)
                    self.counter.reset()
                if self.counter.value != 0:
                    if self.counter.value % 80 == 0 and self.counter.value < 2240:
                        if self.difficulty == 2:
                            self.sprite.prettyPattern(1)
                            self.counter.value += 1
                            self.cooldown.start()
                        else:
                            self.sprite.shoot_at_player()

        else:
            if self.counter.value % 200 == 0:
                pattern = random.randint(1, 2)
                self.sprite.prettyPattern(pattern)

    def vectorNorm(self,x,y):
        result = math.sqrt(x**2+y**2)
        if result == 0:
            return 1

        return result