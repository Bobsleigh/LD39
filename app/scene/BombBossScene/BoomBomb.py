import pygame
import os
import random
import math
from app.settings import *
from ldLib.collision.collisionMask import CollisionMask
from ldLib.tools.ImageBox import ImageBox
from ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from ldLib.Sprites.Player.IdleState import IdleState
from app.scene.BombBossScene.ExplodedBomb import ExplodedBomb
from ldLib.tools.Counter import Counter


class BoomBomb(pygame.sprite.Sprite):
    def __init__(self, destination_x, destination_y, initial_x, initial_y, sceneData, max_health=10):
        super().__init__()

        self.name = "BoomBomb"

        self.imageBase = pygame.image.load(os.path.join('img', 'bomb.png'))
        self.imageBase.set_colorkey(COLORKEY)

        self.imageShapeLeft = None
        self.imageShapeRight = None

        self.setShapeImage()
        self.image = self.imageShapeRight

        self.imageTransparent = ImageBox().rectSurface((32, 32), WHITE, 3)
        self.imageTransparent.set_colorkey(COLORKEY)

        self.rect = self.image.get_rect()  # Position centrée du player
        self.x = initial_x
        self.x_destination = destination_x
        self.y = initial_y
        self.y_destination = destination_y
        self.rect.x = initial_x
        self.rect.y = initial_y
        self.previousX = initial_x
        self.previousY = initial_y

        self.speedx = 0
        self.speedy = 0
        self.maxSpeedx = 600
        self.maxSpeedyUp = 600
        self.maxSpeedyDown = 600
        self.accx = 1
        self.accy = 1
        self.jumpSpeed = 15
        self.springJumpSpeed = 25

        self.isFrictionApplied = False
        self.isCollisionApplied = True
        self.facingSide = RIGHT
        self.friendly = True

        self.rightPressed = False
        self.leftPressed = False
        self.upPressed = False
        self.downPressed = False
        self.leftShiftPressed = False
        self.spacePressed = False
        self.leftMousePressed = False
        self.rightMousePressed = False

        self.mapData = sceneData

        self.isAlive = True
        self.lifespan = random.randint(50, 80)

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.collisionRules = []
        self.collisionRules.append(CollisionWithNothing())  # Gotta be first in the list to work properly
        self.collisionRules.append(CollisionWithSolid())

        self._state = IdleState()
        self.counter = Counter()
        # self.nextState = None

    def setShapeImage(self):
        self.imageShapeLeft = pygame.transform.flip(self.imageBase, True, False)
        self.imageShapeRight = self.imageBase

    def update(self):
        self.capSpeed()

        self.previousX = self.x
        self.previousY = self.y

        self.moveX()
        self.moveY()
        self.rect.x = self.x
        self.rect.y = self.y

        if self.speedx > 0:
            self.image = self.imageShapeRight
            self.facingSide = RIGHT
        if self.speedx < 0:
            self.image = self.imageShapeLeft
            self.facingSide = LEFT

        self.updateCollisionMask()
        self.updatePressedKeys()

        self.counter.value += 1
        if self.counter.value > self.lifespan:
            self.Boom()

    def moveX(self):
        self.x = math.floor((7 * self.x + self.x_destination)/8)
        self.collisionMask.rect.x = self.x
        for rule in self.collisionRules:
            rule.onMoveX(self)

    def moveY(self):
        self.y = math.floor((7 * self.y + self.y_destination)/8)
        self.collisionMask.rect.y = self.y
        for rule in self.collisionRules:
            rule.onMoveY(self)

    def capSpeed(self):
        if self.speedx > 0 and self.speedx > self.maxSpeedx:
            self.speedx = self.maxSpeedx
        if self.speedx < 0 and self.speedx < -self.maxSpeedx:
            self.speedx = -self.maxSpeedx
        if self.speedy > 0 and self.speedy > self.maxSpeedyDown:
            self.speedy = self.maxSpeedyDown
        if self.speedy < 0 and self.speedy < -self.maxSpeedyUp:
            self.speedy = -self.maxSpeedyUp

    def updateSpeedRight(self):
        self.speedx += self.accx

    def updateSpeedLeft(self):
        self.speedx -= self.accx

    def updateSpeedUp(self):
        self.speedy -= self.accy

    def updateSpeedDown(self):
        self.speedy += self.accy

    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y

    def stop(self):
        self.speedx = 0
        self.speedy = 0

    def dead(self):
        self.isAlive = False
        self.kill()

    def Boom(self):

        exploded_bomb = ExplodedBomb(self.rect.centerx, self.rect.centery, self.mapData)
        self.mapData.allSprites.add(exploded_bomb)
        self.mapData.enemyProjectiles.add(exploded_bomb)
        self.mapData.camera.add(exploded_bomb)
        self.dead()

    def onCollision(self, collidedWith, sideOfCollision,limit=0):
        if collidedWith == SOLID:
            if sideOfCollision == RIGHT:
                #On colle le player sur le mur à droite
                self.x = self.previousX
                self.rect.x = self.x
                self.updateCollisionMask()
                self.speedx = 0
                self.rect.right += self.mapData.tmxData.tilewidth - (self.collisionMask.rect.right % self.mapData.tmxData.tilewidth) - 1
            if sideOfCollision == LEFT:
                self.x = self.previousX
                self.rect.x = self.x
                self.updateCollisionMask()
                self.speedx = 0
                self.rect.left -= (self.collisionMask.rect.left % self.mapData.tmxData.tilewidth)  # On colle le player sur le mur de gauche
            if sideOfCollision == DOWN:
                self.y = self.previousY
                self.rect.y = self.y
                self.updateCollisionMask()
                self.speedy = 0
            if sideOfCollision == UP:
                self.y = self.previousY
                self.rect.y = self.y
                self.updateCollisionMask()
                self.speedy = 0

    # def notify(self, event):
    #     self.nextState = self.state.handleInput(self, event)

        # if self.nextState != None:
        #     self.state.exit(self)
        #     self.state = self.nextState
        #     self.state.enter(self)
        #     self.nextState = None

    # @property
    # def state(self):
    #     return self._state
    #
    # @state.setter
    # def state(self, value):
    #     self._state.exit(self)
    #     self._state = value
    #     self._state.enter(self)


    def updatePressedKeys(self):
        if self.rightPressed:
            self.updateSpeedRight()
        if self.leftPressed:
            self.updateSpeedLeft()
        if self.upPressed:
            self.updateSpeedUp()
        if self.downPressed:
            self.updateSpeedDown()
        if self.leftMousePressed:
            pass
        if self.rightMousePressed:
            pass
        if self.leftShiftPressed:
            pass
        if self.spacePressed:
            pass

    def jump(self):
        self.speedy = -self.jumpSpeed
