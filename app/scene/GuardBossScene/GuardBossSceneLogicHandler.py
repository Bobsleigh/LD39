__author__ = 'Bobsleigh'

from ldLib.scene.LogicHandler import LogicHandler
from app.scene.TopDownPhysics import TopDownPhysics
from ldLib.collision.collisionNotifySprite import collisionNotifySprite
from app.settings import *
from app.sprites.Bullet import Bullet
import pygame



class BombBossSceneLogicHandler(LogicHandler):
    def __init__(self, gameData):
        super().__init__(gameData)
        self.physics = TopDownPhysics(gameData.sceneData)

    def handle(self):
        super().handle()
        self.physics.update()
        self.handleFriendlyBulletCollision()
        self.handleBulletCollision()

    def handleCollision(self):
        for sprite in self.gameData.sceneData.allSprites:
            collisionNotifySprite(sprite, SOLID, self.gameData.sceneData)

    def handleBulletCollision(self):
        collisionList = pygame.sprite.spritecollide(self.sceneData.player, self.sceneData.enemyProjectiles, False)
        for bullet in collisionList:
            if isinstance(bullet, Bullet):
                bullet.detonate()
            self.sceneData.player.hurt(10)

    def handleFriendlyBulletCollision(self):
        collisionList = pygame.sprite.spritecollide(self.sceneData.boss, self.sceneData.friendlyBullets, False)
        for bullet in collisionList:
            bullet.detonate()
            self.sceneData.boss.hurt(10)

    def explodingBombCollision(self):
        collisionList = pygame.sprite.spritecollide(self.sceneData.player, self.sceneData.laserGroup, False)
        for laser in collisionList:
            self.sceneData.player.hurt(laser.damage)
