import pygame, os
from app.settings import *
from app.sprites.LevelHUD import LevelHUD
from app.scene.LevelSceneData import LevelSceneData
from app.scene.SecondBossScene.Boss2 import Boss2
from app.scene.SecondBossScene.LaserTurret import LaserTurret
from app.scene.SecondBossScene.ChargePad import ChargePad
from app.sprites.PlayerPlateform import PlayerPlateform
from app.scene.PlayerDeadFadeOut import PlayerDeadFadeOut
from app.scene.FinalBossDeadFadeOut import FinalBossDeadFadeOut


class SecondBossSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("LaserBossRoom", "InZone_01")

        self.sceneName = LASER_BOSS_LEVEL
        self.nextLevel = ENDING_SCENE

        self.laserGroup = pygame.sprite.Group()
        self.bossGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.turretGroup = pygame.sprite.Group()
        self.chargePadGroup = pygame.sprite.Group()

        self.chargePad = ChargePad(300, 300, self)
        self.chargePadGroup.add(self.chargePad)
        self.allSprites.add(self.chargePad)
        self.camera.add(self.chargePad)

        self.boss = Boss2(200, 200, self)
        self.bossGroup.add(self.boss)
        self.enemyGroup.add(self.boss)
        self.allSprites.add(self.boss)
        self.camera.add(self.boss)

        self.turret1 = LaserTurret(600, 100, self)
        self.turretGroup.add(self.turret1)
        self.allSprites.add(self.turret1)
        self.enemyGroup.add(self.turret1)
        self.camera.add(self.turret1)
        self.turret2 = LaserTurret(370, 500, self)
        self.turretGroup.add(self.turret2)
        self.allSprites.add(self.turret2)
        self.enemyGroup.add(self.turret2)
        self.camera.add(self.turret2)
        self.turret3 = LaserTurret(100, 200, self)
        self.turretGroup.add(self.turret3)
        self.allSprites.add(self.turret3)
        self.enemyGroup.add(self.turret3)
        self.camera.add(self.turret3)

        # Hack to draw the player on top of the charge pad
        self.player.kill()
        self.spritesHUD.empty()
        playerInitx = 50
        playerInity = 50
        try:
            playerInitx = self.spawmPointPlayerx
            playerInity = self.spawmPointPlayery
        except AttributeError:
            pass

        self.player = PlayerPlateform(playerInitx, playerInity, self)
        self.camera.add(self.player)

        self.addHUD()

        #self.musicName = "BoxCat_Games_-_25_-_Victory.mp3"
        self.musicName = "Creo_-_Ahead_Of_The_Curve-TRIM.wav"

    def LaserBossIsDead(self):
        self.nextScene = self.nextLevel
        self.endSceneCause = BOSS_DEAD

    def beforeLeavingScene(self, screen):
        if self.endSceneCause == BOSS_DEAD:
            FinalBossDeadFadeOut(screen)

        if self.endSceneCause == PLAYER_DEAD:
            PlayerDeadFadeOut(screen)
