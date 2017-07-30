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
        self.handleFriendlyBulletCollision()
        self.handleEnemyCollision()
        self.physics.update()

    def handleLaserCollision(self):
        collisionList = pygame.sprite.spritecollide(self.sceneData.player, self.sceneData.laserGroup, False)
        for laser in collisionList:
            self.sceneData.player.hurt(laser.damage)
            self.sceneData.boss.AI.wasHurt = True   # Hack to make the state change from ShootingLaser to MoveToCenterMap

    def handleEnemyCollision(self):
        collisionList = pygame.sprite.spritecollide(self.sceneData.player, self.sceneData.enemyGroup, False)
        for enemy in collisionList:
            self.sceneData.player.hurt(enemy.touchDamage)
            self.sceneData.boss.AI.wasHurt = True   # Hack to make the state change from ShootingLaser to MoveToCenterMap

    def handleFriendlyBulletCollision(self):
        collisionDict = pygame.sprite.groupcollide(self.sceneData.bossGroup, self.sceneData.friendlyBullets, False, True)
        for boss in collisionDict:
            for bullet in collisionDict[boss]:
                boss.hurt(bullet.attackDMG)