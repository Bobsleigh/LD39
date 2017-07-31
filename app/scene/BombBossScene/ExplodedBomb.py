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
from ldLib.tools.Counter import Counter


class ExplodedBomb(pygame.sprite.Sprite):
    def __init__(self, x_center, y_center, sceneData, max_health=10):
        super().__init__()

        self.name = "ExplodedBomb"

        self.imageBase = pygame.image.load(os.path.join('img', 'explosion1.png'))
        self.imageBase.set_colorkey(COLORKEY)

        self.imageShapeLeft = None
        self.imageShapeRight = None

        self.setShapeImage()
        self.image = self.imageShapeRight

        self.rect = self.image.get_rect()  # Position centrée du player
        self.x = x_center
        self.y = y_center
        self.rect.centerx = x_center
        self.rect.centery = y_center

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
        self.counter.value += 1
        old_centerx = self.rect.centerx
        old_centery = self.rect.centery
        if self.counter.value == 15:
            self.image = pygame.image.load(os.path.join('img', 'explosion2.png'))
            self.rect = self.image.get_rect()
            self.rect.centerx = old_centerx
            self.rect.centery = old_centery
        if self.counter.value == 25:
            self.image = pygame.image.load(os.path.join('img', 'explosion3.png'))
            self.rect = self.image.get_rect()
            self.rect.centerx = old_centerx
            self.rect.centery = old_centery
        if self.counter.value == 40:
            self.image = pygame.image.load(os.path.join('img', 'explosion2.png'))
            self.rect = self.image.get_rect()
            self.rect.centerx = old_centerx
            self.rect.centery = old_centery
        if self.counter.value == 60:
            self.dead()

    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y

    def dead(self):
        self.isAlive = False
        self.kill()
