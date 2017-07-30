import pygame

from app.scene.LevelSceneData import LevelSceneData
from app.settings import *

class CorridorSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("TestTmxData", "InZone_01")
        self.sceneName = CORRIDOR_LEVEL_1
        self.nextLevel = INSTRUCTION_SCENE

        self.sceneName = TEST_TMX_SCENE
        self.nextLevel = CORRIDOR_LEVEL_1
