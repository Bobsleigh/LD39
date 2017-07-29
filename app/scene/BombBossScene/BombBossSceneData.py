from app.scene.SecondBossScene.Boss2 import Boss2
from ldLib.scene.SceneDataTMX import SceneDataTMX
from app.scene.corridorScene.PlayerPlateform import PlayerPlateform


class BombBossSceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("BossRoom1", "InZone_01")

        playerInitx = 50
        playerInity = 50
        try:
            playerInitx = self.spawmPointPlayerx
            playerInity = self.spawmPointPlayery
        except AttributeError:
            pass

        self.player = PlayerPlateform(playerInitx, playerInity, self)
        self.camera.add(self.player)

        self.boss = Boss2(playerInitx, playerInity, self)
        self.allSprites.add(self.boss)
        self.camera.add(self.boss)