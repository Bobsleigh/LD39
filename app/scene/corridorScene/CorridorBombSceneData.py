import pygame

from app.scene.LevelSceneData import LevelSceneData
from app.settings import *


class CorridorBombSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("BombCorridor", "InZone_01")
        self.sceneName = BOMB_CORRIDOR_LEVEL
        self.nextLevel = BOMB_BOSS_LEVEL
