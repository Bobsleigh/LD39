import pygame

from app.scene.LevelSceneData import LevelSceneData
from app.settings import *
from ldLib.GUI.WrappedTextBox import WrappedTextBox


class CorridorSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("TestTmxData", "InZone_01")
        self.sceneName = TEST_TMX_SCENE
        self.nextLevel = CORRIDOR_LEVEL_1
