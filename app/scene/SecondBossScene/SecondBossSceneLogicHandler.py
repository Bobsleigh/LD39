__author__ = 'Bobsleigh'

import pygame
from ldLib.scene.LogicHandler import LogicHandler
from app.scene.TopDownPhysics import TopDownPhysics
from app.scene.SecondBossScene.Laser import Laser
from ldLib.collision.collisionNotifySprite import collisionNotifySprite
from app.settings import *

class SecondBossSceneLogicHandler(LogicHandler):
    def __init__(self, gameData):
        super().__init__(gameData)
        self.physics = TopDownPhysics(gameData.sceneData)

    def handle(self):
        super().handle()
        self.handleLaserCollision()
        self.physics.update()

    def handleLaserCollision(self):
        collisionList = pygame.sprite.spritecollide(self.sceneData.player, self.sceneData.laserGroup, False)
        for laser in collisionList:
            self.sceneData.player.hurt(laser.damage)