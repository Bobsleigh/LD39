import pygame

from app.scene.LevelSceneData import LevelSceneData
from app.settings import *
from ldLib.GUI.WrappedTextBox import WrappedTextBox


class CorridorGuardSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("GuardCorridorRoom", "InZone_01")
        self.sceneName = GUARD_CORRIDOR_LEVEL
        self.nextLevel = GUARD_BOSS_LEVEL

        self.messageBoxes = list()
        self.messageBoxes.append([WrappedTextBox(MESSAGE_BOX_POSITION, MESSAGE_BOX_DIMENSION, "I've gone past the barbed fence. There's no going back.         I will be able to dethrone Kleido."),False])
        self.messageBoxes.append([WrappedTextBox(MESSAGE_BOX_POSITION, MESSAGE_BOX_DIMENSION, "I hope no one's guarding the door. It would be a shame.        For them."),False])

        self.musicName = "BoxCat_Games_-_23_-_Trace_Route.wav"

        self.addHUD()