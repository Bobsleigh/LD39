from app.settings import *
from app.sprites.PlayerPlateform import PlayerPlateform
from ldLib.scene.SceneDataTMX import SceneDataTMX


class CorridorLevel1SceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("TestOut", "InZone_01")

        playerInitx = 50
        playerInity = 50
        try:
            playerInitx = self.spawmPointPlayerx
            playerInity = self.spawmPointPlayery
        except AttributeError:
            pass

        self.player = PlayerPlateform(playerInitx, playerInity, self)
        self.camera.add(self.player)

        self.nextLevel = TITLE_SCENE
