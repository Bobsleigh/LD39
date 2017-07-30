import pygame
from app.settings import *

from app.scene.LevelSceneData import LevelSceneData
from app.scene.SecondBossScene.Boss2 import Boss2

class SecondBossSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("TestTmxData", "InZone_01")
        self.sceneName = LASER_BOSS_LEVEL
        self.nextLevel = INSTRUCTION_SCENE

        self.laserGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()

        self.boss = Boss2(200, 200, self)
        self.enemyGroup.add(self.boss)
        self.allSprites.add(self.boss)
        self.camera.add(self.boss)