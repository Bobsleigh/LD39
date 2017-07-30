import pygame

from app.scene.LevelSceneData import LevelSceneData
from app.scene.PlayerDeadFadeOut import PlayerDeadFadeOut
from app.settings import *
from app.sprites.LevelHUD import LevelHUD
from app.sprites.PlayerPlateform import PlayerPlateform
from ldLib.scene.SceneDataTMX import SceneDataTMX


class CorridorSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("TestTmxData", "InZone_01")
        self.sceneName = TEST_TMX_SCENE
        self.nextLevel = CORRIDOR_LEVEL_1
