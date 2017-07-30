import pygame

from app.scene.SecondBossScene.Boss2 import Boss2
from app.scene.SecondBossScene.LaserTurret import LaserTurret
from app.sprites.LevelHUD import LevelHUD
from app.sprites.PlayerPlateform import PlayerPlateform
from ldLib.scene.SceneDataTMX import SceneDataTMX


class SecondBossSceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("TestTmxData", "InZone_01")

        self.laserGroup = pygame.sprite.Group()
        self.bossGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.turretGroup = pygame.sprite.Group()

        playerInitx = 50
        playerInity = 50
        try:
            playerInitx = self.spawmPointPlayerx
            playerInity = self.spawmPointPlayery
        except AttributeError:
            pass

        self.player = PlayerPlateform(playerInitx, playerInity, self)
        self.camera.add(self.player)

        self.boss = Boss2(200, 200, self)
        self.bossGroup.add(self.boss)
        self.enemyGroup.add(self.boss)
        self.allSprites.add(self.boss)
        self.camera.add(self.boss)

        # turret = LaserTurret(100, 200, self)
        # self.turretGroup.add(turret)
        # self.allSprites.add(turret)
        # self.camera.add(turret)
        # turret = LaserTurret(400, 400, self)
        # self.turretGroup.add(turret)
        # self.allSprites.add(turret)
        # self.camera.add(turret)

        LevelHUD(self,self.player)
