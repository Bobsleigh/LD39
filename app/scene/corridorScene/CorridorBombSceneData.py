import pygame

from app.scene.LevelSceneData import LevelSceneData
from app.settings import *
from ldLib.GUI.WrappedTextBox import WrappedTextBox


class CorridorBombSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("BombCorridor", "InZone_01")
        self.sceneName = BOMB_CORRIDOR_LEVEL
        self.nextLevel = BOMB_BOSS_LEVEL

        self.messageBoxes = list()
        self.messageBoxes.append([WrappedTextBox(MESSAGE_BOX_POSITION, MESSAGE_BOX_DIMENSION, "I'm in! Next stop: General Dreetus, the last stand before Kleido."),False])
        self.messageBoxes.append([WrappedTextBox(MESSAGE_BOX_POSITION, MESSAGE_BOX_DIMENSION, "After all they've done, I should serve them both shocking justice."),False])

        self.musicName = "BoxCat_Games_-_23_-_Trace_Route.wav"

        self.addHUD()