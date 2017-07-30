import pygame
from app.settings import *

from app.scene.LevelSceneData import LevelSceneData
from app.scene.SecondBossScene.Boss2 import Boss2
from app.scene.SecondBossScene.LaserTurret import LaserTurret

class SecondBossSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("TestTmxData", "InZone_01")
        self.sceneName = LASER_BOSS_LEVEL
        self.nextLevel = INSTRUCTION_SCENE

        self.laserGroup = pygame.sprite.Group()
        self.bossGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.turretGroup = pygame.sprite.Group()

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