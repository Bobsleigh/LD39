import pygame

from app.scene.LevelSceneData import LevelSceneData
from app.settings import *
from ldLib.GUI.WrappedTextBox import WrappedTextBox


class CorridorLaserSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("BombCorridor", "InZone_01")
        self.sceneName = LASER_CORRIDOR_LEVEL
        self.nextLevel = LASER_BOSS_LEVEL

        self.messageBoxes = list()
        self.messageBoxes.append([WrappedTextBox(MESSAGE_BOX_POSITION, MESSAGE_BOX_DIMENSION, "That guy was tough! Let's take down the superadmiral now, who's with me?"),False])
        self.messageBoxes.append([WrappedTextBox(MESSAGE_BOX_POSITION, MESSAGE_BOX_DIMENSION, "Oh right, I'm doing this alone..."),False])

