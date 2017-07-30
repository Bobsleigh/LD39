import pygame

from app.scene.LevelSceneData import LevelSceneData
from app.scene.SecondBossScene.LaserTurret import LaserTurret
from app.settings import *
from ldLib.GUI.WrappedTextBox import WrappedTextBox


class CorridorSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("TestTmxData", "InZone_01")
        self.sceneName = TEST_TMX_SCENE
        self.nextLevel = CORRIDOR_LEVEL_1

        self.addHUD()

        self.musicName = "BoxCat_Games_-_23_-_Trace_Route.wav"

        self.messageBoxes = list()
        self.messageBoxes.append(
            [WrappedTextBox(MESSAGE_BOX_POSITION, MESSAGE_BOX_DIMENSION, "That guy was tough, but not as tough as me!"),
             False])
        self.messageBoxes.append([WrappedTextBox(MESSAGE_BOX_POSITION, MESSAGE_BOX_DIMENSION,
                                                 "The Superadmiral doesn't know what's coming."), False])

        self.musicName = "BoxCat_Games_-_23_-_Trace_Route.wav"

        self.turretGroup = pygame.sprite.Group()
        self.bossGroup = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()

        self.turret1 = LaserTurret(600, 100, self)
        self.turretGroup.add(self.turret1)
        self.allSprites.add(self.turret1)
        self.enemyGroup.add(self.turret1)
        self.camera.add(self.turret1)
