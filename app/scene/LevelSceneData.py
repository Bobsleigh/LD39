import pygame

from app.scene.PlayerDeadFadeOut import PlayerDeadFadeOut
from app.settings import *
from app.sprites.LevelHUD import LevelHUD
from app.sprites.PlayerPlateform import PlayerPlateform
from ldLib.scene.SceneDataTMX import SceneDataTMX


class LevelSceneData(SceneDataTMX):
    def __init__(self,mapName, nameInZone):
        super().__init__(mapName, nameInZone )
        self.sceneName = None
        self.nextLevel = TITLE_SCENE

        self.friendlyBullets = pygame.sprite.Group()

        playerInitx = 50
        playerInity = 50
        try:
            playerInitx = self.spawmPointPlayerx
            playerInity = self.spawmPointPlayery
        except AttributeError:
            pass

        self.player = PlayerPlateform(playerInitx, playerInity, self)
        self.camera.add(self.player)

        self.boss = None

        LevelHUD(self, self.player,self.boss)

    def playerIsDead(self):
        self.nextScene = self.sceneName
        self.endSceneCause = PLAYER_DEAD

    def beforeLeavingScene(self, screen):
        if self.endSceneCause == PLAYER_DEAD:
            PlayerDeadFadeOut(screen)

