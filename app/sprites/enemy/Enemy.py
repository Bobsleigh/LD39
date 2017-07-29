import pygame
from ldLib.collision.collisionMask import CollisionMask

from app.settings import *
from ldLib.animation.Animation import Animation
from ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.name = "enemy"
        self.type = "enemy"

        self.imageEnemy = pygame.Surface((1, 1))
        self.imageEnemy.set_alpha(0)
        self.image = self.imageEnemy

        self.frames = [self.imageEnemy]
        self.animation = Animation(self.frames, 100)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.isPhysicsApplied = False
        self.isCollisionApplied = False

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.collisionRules = []
        self.collisionRules.append(CollisionWithNothing())  # Gotta be first in the list to work properly

        self.soundDead = None

        self.dictProperties = {}

        self.attackDMG = 0
        self.friendly = False

        self.mapData = None

        self.bounty = 0

    def setMapData(self, mapData):
        self.mapData = mapData

    def update(self):
        self.moveX()
        self.moveY()

        self.animation.update(self)
        self.updateCollisionMask()


    def moveX(self):
        self.x += self.speedx
        self.collisionMask.rect.x = self.x
        for rule in self.collisionRules:
            rule.onMoveX(self)


    def moveY(self):
        self.y += self.speedy
        self.collisionMask.rect.y = self.y
        for rule in self.collisionRules:
            rule.onMoveY(self)

    def applyAI(self):
        pass

    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y

    def isHit(self,dmg=0):
        pass

    def dead(self):
        if self.mapData != None:
            self.mapData.gold += self.bounty

        self.kill()

    def notify(self, event):
        pass

    def attackOnCollision(self):
        pass
