from app.scene.BombBossScene.BombBoss import BombBoss
from app.sprites.LevelHUD import LevelHUD
from app.sprites.PlayerPlateform import PlayerPlateform
from ldLib.scene.SceneDataTMX import SceneDataTMX


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

        self.boss = BombBoss(playerInitx, 300, self)
        self.allSprites.add(self.boss)
        self.enemyProjectiles.add(self.boss)
        self.camera.add(self.boss)

        LevelHUD(self,self.player)
