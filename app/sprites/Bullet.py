import os
import pygame

from app.settings import *
from app.sprites.enemy.Enemy import Enemy
from ldLib.collision.CollisionRules.CollisionWithSolidDetonate import CollisionWithSolidDetonate


class Bullet(Enemy):
    def __init__(self, x, y, speedx, speedy, sceneData, friendly=True):
        super().__init__(x, y)

        self.mapData = sceneData

        self.name = "bullet"

        self.image = pygame.image.load(os.path.join('img', 'bomb-zap-explode.png'))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

        # if direction == RIGHT:
        #     self.speedx = 10
        #     self.image = self.imageBulletRight[0]
        #     self.imageBulletList = self.imageBulletRight
        #     self.rect.x = x
        # elif direction == LEFT:
        #     self.speedx = -10
        #     self.image = self.imageBulletLeft[0]
        #     self.imageBulletList = self.imageBulletLeft
        #     self.rect.x = x - self.rect.width
        self.speedx = speedx
        self.speedy = speedy

        self.animation = None
        self.attackDMG = 1

        self.friendly = friendly
        self.isCollisionApplied = True

        self.collisionRules.append(CollisionWithSolidDetonate())  # Gotta be first in the list to work properly

    def update(self):

        self.moveX()
        self.moveY()

        self.rect.x = self.x
        self.rect.y = self.y

        if self.animation is not None:
            next(self.animation)
        self.updateCollisionMask()

    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y

    def onCollision(self, collidedWith):
        if collidedWith == SOLID:
            self.detonate()

    def hitEnemy(self):
        self.detonate()

    def detonate(self):
        self.kill()

class PlayerBullet(Bullet):
    def __init__(self, x, y, speedx, speedy, sceneData):
        super().__init__(x, y, speedx, speedy, sceneData)

        self.image = pygame.image.load(os.path.join('img', 'lutecia-bullet.png'))

        self.attackDMG = PLAYER_BULLET_DAMAGE
