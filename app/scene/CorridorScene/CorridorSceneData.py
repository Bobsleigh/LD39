import pygame

from app.settings import *
from app.sprites.PlayerPlateform import PlayerPlateform
from ldLib.GUI.Peanut import LifeBar
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

        self.addHUD()

    def addHUD(self):
        lifeBar = LifeBar(self.player,20,20,SCREEN_WIDTH/5,SCREEN_HEIGHT/30)
        self.spritesHUD.add(lifeBar)