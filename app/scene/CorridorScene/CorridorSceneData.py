import pygame

from app.settings import *
from app.sprites.LevelHUD import LevelHUD
from app.sprites.PlayerPlateform import PlayerPlateform
from ldLib.scene.SceneDataTMX import SceneDataTMX


class CorridorSceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("TestTmxData", "InZone_01")

        self.friendlyBullets = pygame.sprite.Group()

        playerInitx = 50
        playerInity = 50
        try:
            playerInitx = self.spawmPointPlayerx
            playerInity = self.spawmPointPlayery
        except AttributeError:
            pass

        self.nextLevel = CORRIDOR_LEVEL_1

        self.player = PlayerPlateform(playerInitx, playerInity, self)
        self.camera.add(self.player)

        LevelHUD(self,self.player)
