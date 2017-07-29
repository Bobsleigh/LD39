__author__ = 'Bobsleigh'

import pygame
from ldLib.Sprites.SecondBoss.EnemyState import EnemyState
from app.scene.SecondBossScene.Laser import Laser
from app.settings import *

class ShootingLaserState(EnemyState):
    def __init__(self, sprite, isRightLeft, sceneData):
        super().__init__()
        self.sceneData = sceneData
        self.isRightLeft = isRightLeft
        self.laser = Laser(sprite.rect.x, sprite.rect.y, sceneData)

    def update(self, sprite, mapData):
        if self.isRightLeft:
            self.laser.rect.y = sprite.rect.y
        else:
            self.laser.rect.x = sprite.rect.x

    def enter(self, sprite):
        self.sceneData.allSprites.add(self.laser)
        self.sceneData.camera.add(self.laser)

    def exit(self, sprite):
        self.laser.kill()
