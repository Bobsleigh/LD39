__author__ = 'Bobsleigh'

import pygame, math
from ldLib.Sprites.SecondBoss.EnemyState import EnemyState
from app.scene.SecondBossScene.Laser import Laser
from app.settings import *

class ShootingAllLasersState(EnemyState):
    def __init__(self, sprite, sceneData):
        super().__init__()
        self.sceneData = sceneData
        self.laser1 = Laser(sprite.rect.right, sprite.rect.centery, sceneData)
        self.laser2 = Laser(sprite.rect.left, sprite.rect.centery, sceneData, True)
        self.laser1.rect.centery = sprite.rect.centery
        self.laser2.rect.centery = sprite.rect.centery

        self.laser3 = Laser(sprite.rect.centerx, sprite.rect.bottom, sceneData)
        self.laser4 = Laser(sprite.rect.centerx, sprite.rect.top, sceneData)
        self.laser3.rotate(90)
        self.laser4.rotate(90)

        self.laser3.rect.x = sprite.rect.centerx - self.laser3.rect.height/2
        self.laser4.rect.x = sprite.rect.centerx - self.laser4.rect.height/2
        self.laser4.rect.y = sprite.rect.top - self.laser4.rect.width
        self.laser3.updateCollisionMask()
        self.laser4.updateCollisionMask()

    def update(self, sprite, mapData):
        self.laser1.rect.x = sprite.rect.right
        self.laser1.rect.centery = sprite.rect.centery
        self.laser2.rect.right = sprite.rect.left
        self.laser2.rect.centery = sprite.rect.centery


        self.laser3.rect.x = sprite.rect.centerx - self.laser3.rect.width/2
        self.laser3.rect.y = sprite.rect.bottom
        self.laser4.rect.x = sprite.rect.centerx - self.laser4.rect.width/2
        self.laser4.rect.y = sprite.rect.top - self.laser4.image.get_rect().height

    def enter(self, sprite):
        sprite.soundLaser.play()
        self.sceneData.laserGroup.add(self.laser1)
        self.sceneData.allSprites.add(self.laser1)
        self.sceneData.camera.add(self.laser1)

        self.sceneData.laserGroup.add(self.laser2)
        self.sceneData.allSprites.add(self.laser2)
        self.sceneData.camera.add(self.laser2)

        self.sceneData.laserGroup.add(self.laser3)
        self.sceneData.allSprites.add(self.laser3)
        self.sceneData.camera.add(self.laser3)

        self.sceneData.laserGroup.add(self.laser4)
        self.sceneData.allSprites.add(self.laser4)
        self.sceneData.camera.add(self.laser4)

    def exit(self, sprite):
        sprite.soundLaser.stop()
        self.laser1.kill()
        self.laser2.kill()
        self.laser3.kill()
        self.laser4.kill()
