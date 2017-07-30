import math, random
from app.settings import *
from ldLib.tools.Counter import Counter
from app.scene.SecondBossScene.LaserTurret import LaserTurret
from ldLib.Sprites.SecondBoss.IdleState import IdleState
from ldLib.Sprites.SecondBoss.MoveUpState import MoveUpState
from ldLib.Sprites.SecondBoss.MoveDownState import MoveDownState
from ldLib.Sprites.SecondBoss.MoveRightState import MoveRightState
from ldLib.Sprites.SecondBoss.MoveLeftState import MoveLeftState
from ldLib.Sprites.SecondBoss.MoveRandomState import MoveRandomState
from ldLib.Sprites.SecondBoss.MoveXTowardPlayer import MoveXTowardPlayer
from ldLib.Sprites.SecondBoss.MoveYTowardPlayer import MoveYTowardPlayer
from ldLib.Sprites.SecondBoss.MoveToMapCenterState import MoveToMapCenterState
from ldLib.Sprites.SecondBoss.ShootingLaserState import ShootingLaserState
from ldLib.Sprites.SecondBoss.ShootingAllLasersState import ShootingAllLasersState

class Boss2AI:
    def __init__(self, sprite, mapData):
        self.sprite = sprite
        self.mapData = mapData

        self.counter = Counter()
        self.returnCenterCounter = Counter()
        self.laserCounter = Counter()
        self._state = IdleState()
        self.state = IdleState()
        self._laserState = IdleState()
        self.laserState = IdleState()
        self.randomMoveTime = random.randint(60, 480)
        self.lastFrameHealth = sprite.currentHealth
        self.difficulty = 0

        self.wasHurt = False
        self.numberOfTurretsDown = 0

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state.exit(self)
        self._state = value
        self._state.enter(self)

    @property
    def laserState(self):
        return self._laserState

    @laserState.setter
    def laserState(self, value):
        self._laserState.exit(self.sprite)
        self._laserState = value
        self._laserState.enter(self.sprite)

    def update(self):
        self.counter.value += 1
        self.laserCounter.value += 1
        if isinstance(self.state, MoveToMapCenterState):
            self.returnCenterCounter.value += 1
        self.chooseState()

        self.state.update(self.sprite, self.mapData)
        self.updateLaser()
        self.laserState.update(self.sprite, self.mapData)
        self.updateDifficulty()

    def updateDifficulty(self):
        if (self.sprite.currentHealth/self.sprite.maxHealth) < 0.3:
            self.difficulty = 3
            if self.numberOfTurretsDown == 2:
                self.mapData.turret1.needToOpen = True
                self.numberOfTurretsDown += 1
        if (self.sprite.currentHealth/self.sprite.maxHealth) < 0.5:
            self.difficulty = 2
            if self.numberOfTurretsDown == 1:
                self.mapData.turret2.needToOpen = True
                self.numberOfTurretsDown += 1

        elif (self.sprite.currentHealth/self.sprite.maxHealth) < 0.7:
            self.difficulty = 1
            if self.numberOfTurretsDown == 0:
                self.mapData.turret3.needToOpen = True
                self.numberOfTurretsDown += 1

    def chooseState(self):
        if self.counter.value == 1:
            self.state = MoveRandomState(60,20)
        if self.counter.value == self.randomMoveTime:
            rnd = random.randint(0,1)
            if rnd == 0:
                self.state = MoveXTowardPlayer(self.mapData)
                self.laserState = ShootingLaserState(self.sprite , False, self.mapData)
                if self.difficulty >= 1:
                    self.laserState = ShootingAllLasersState(self.sprite , self.mapData)
            else:
                self.state = MoveYTowardPlayer(self.mapData)
                self.laserState = ShootingLaserState(self.sprite , True, self.mapData)
                if self.difficulty >= 1:
                    self.laserState = ShootingAllLasersState(self.sprite , self.mapData)

        if self.counter.value > self.randomMoveTime:
            if not isinstance(self.state, MoveToMapCenterState):
                if self.wasHurt:
                    self.wasHurt = False
                    self.state = MoveToMapCenterState()
                    self.laserState = IdleState()
            else:
                if self.sprite.rect.centerx < (self.mapData.tmxData.width * self.mapData.tmxData.tilewidth)/2 + 5 and self.sprite.rect.centerx > (self.mapData.tmxData.width * self.mapData.tmxData.tilewidth)/2 - 5 and self.sprite.rect.centery > (self.mapData.tmxData.height * self.mapData.tmxData.tileheight)/2 - 5 and self.sprite.rect.centery < (self.mapData.tmxData.height * self.mapData.tmxData.tileheight)/2 + 5:
                    self.counter.reset()
                    self.returnCenterCounter.reset()

            if self.returnCenterCounter.value > 120:
                self.counter.reset()
                self.returnCenterCounter.reset()
        else:
            if self.wasHurt:
                self.wasHurt = False

    def updateLaser(self):
        pass
        # if self.laserCounter.value == 1:
        #     self.laserState = ShootingLaserState(self.sprite , random.choice([True,False]), self.mapData)
        # elif self.laserCounter.value == 200:
        #     self.laserState = IdleState()
        # elif self.laserCounter.value == 310:
        #     self.laserCounter.reset()

    def vectorNorm(self,x,y):
        result = math.sqrt(x**2+y**2)
        if result == 0:
            return 1

        return result