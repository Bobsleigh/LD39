__author__ = 'Bobsleigh'

import pygame, math
from ldLib.Sprites.SecondBoss.EnemyState import EnemyState
from app.scene.SecondBossScene.Laser import Laser
from app.settings import *

class ShootingLaserState(EnemyState):
    def __init__(self, sprite, isRightLeft, sceneData):
        super().__init__()
        self.sceneData = sceneData
        self.isRightLeft = isRightLeft
        if self.isRightLeft:
            self.laser1 = Laser(sprite.rect.right, sprite.rect.centery, sceneData)
            self.laser2 = Laser(sprite.rect.left, sprite.rect.centery, sceneData, True)
            self.laser1.rect.centery = sprite.rect.centery
            self.laser2.rect.centery = sprite.rect.centery
        else:
            self.laser1 = Laser(sprite.rect.centerx, sprite.rect.bottom, sceneData)
            self.laser2 = Laser(sprite.rect.centerx, sprite.rect.top, sceneData)
            # self.laser1.image = pygame.transform.rotate(self.laser1.image, -90)
            # self.laser2.image = pygame.transform.rotate(self.laser2.image, 90)
            self.laser1.rotate(90)
            self.laser2.rotate(90)

            self.laser1.rect.x = sprite.rect.centerx - self.laser2.rect.height/2
            self.laser2.rect.x = sprite.rect.centerx - self.laser2.rect.height/2
            self.laser2.rect.y = sprite.rect.top - self.laser2.rect.width
            self.laser1.updateCollisionMask()
            self.laser2.updateCollisionMask()

    def update(self, sprite, mapData):
        if self.isRightLeft:
            self.laser1.rect.x = sprite.rect.right
            self.laser1.rect.centery = sprite.rect.centery
            self.laser2.rect.right = sprite.rect.left
            self.laser2.rect.centery = sprite.rect.centery

        else:
            self.laser1.rect.x = sprite.rect.centerx - self.laser2.rect.width/2
            self.laser1.rect.y = sprite.rect.bottom
            self.laser2.rect.x = sprite.rect.centerx - self.laser2.rect.width/2
            self.laser2.rect.y = sprite.rect.top - self.laser2.image.get_rect().height

    def enter(self, sprite):
        self.sceneData.laserGroup.add(self.laser1)
        self.sceneData.allSprites.add(self.laser1)
        self.sceneData.camera.add(self.laser1)

        self.sceneData.laserGroup.add(self.laser2)
        self.sceneData.allSprites.add(self.laser2)
        self.sceneData.camera.add(self.laser2)

    def exit(self, sprite):
        self.laser1.kill()
        self.laser2.kill()
