import pygame

from app.settings import *
from app.sprites.LevelHUD import LevelHUD
from app.sprites.PlayerPlateform import PlayerPlateform
from ldLib.scene.SceneDataTMX import SceneDataTMX


class CorridorSceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("TestTmxData", "InZone_01")

        self.sceneName = TEST_TMX_SCENE

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

        LevelHUD(self, self.player)

    def playerIsDead(self):
        self.nextScene = self.sceneName
        self.endSceneCause = PLAYER_DEAD

    def beforeLeavingScene(self, screen):
        if self.endSceneCause == PLAYER_DEAD:
            fontScreen = pygame.font.SysFont(FONT_NAME, 40)
            message = fontScreen.render('You died! Get your revenge on those creeps!', True, BLACK)
            messagePos = [(SCREEN_WIDTH - message.get_width()) / 2,
                          (SCREEN_HEIGHT) / 2]

        screen.blit(message, messagePos)

        pygame.display.flip()
        pygame.time.wait(2000)
