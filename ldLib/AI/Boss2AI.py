import math
from app.settings import *
from ldLib.tools.Counter import Counter
from ldLib.Sprites.SecondBoss.IdleState import IdleState
from ldLib.Sprites.SecondBoss.MoveUpState import MoveUpState
from ldLib.Sprites.SecondBoss.MoveDownState import MoveDownState
from ldLib.Sprites.SecondBoss.MoveRightState import MoveRightState
from ldLib.Sprites.SecondBoss.MoveLeftState import MoveLeftState

class Boss2AI:
    def __init__(self, sprite, mapData):
        self.sprite = sprite
        self.mapData = mapData

        self.counter = Counter()
        self.state = IdleState()

    def update(self):
        self.counter.value += 1
        self.chooseState()
        self.state.update(self.sprite, self.mapData)

    def chooseState(self):
        if self.counter.value == 1:
            self.state = IdleState()
        elif self.counter.value == 80:
            self.state = MoveUpState()
        elif self.counter.value == 120:
            self.state = MoveRightState()
        elif self.counter.value == 160:
            self.state = MoveDownState()
        elif self.counter.value == 200:
            self.state = MoveLeftState()
        elif self.counter.value == 240:
            self.counter.reset()

    def vectorNorm(self,x,y):
        result = math.sqrt(x**2+y**2)
        if result == 0:
            return 1

        return result