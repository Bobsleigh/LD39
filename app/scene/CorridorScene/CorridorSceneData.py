from app.settings import *
from ldLib.scene.SceneDataTMX import SceneDataTMX
from app.scene.corridorScene.PlayerPlateform import PlayerPlateform


class CorridorSceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("TestTmxData", "InZone_01")
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