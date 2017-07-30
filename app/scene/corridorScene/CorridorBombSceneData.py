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
        self.messageBoxes.append([WrappedTextBox(MESSAGE_BOX_POSITION, MESSAGE_BOX_DIMENSION, "Next up is the chief of the army, General Dreetus. The last stand before Superadmiral Kleido."),False])
        self.messageBoxes.append([WrappedTextBox(MESSAGE_BOX_POSITION, MESSAGE_BOX_DIMENSION, "After all he's made us suffer through, let's hope he bites the dust."),False])

