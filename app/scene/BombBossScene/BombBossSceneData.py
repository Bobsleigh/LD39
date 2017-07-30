from app.scene.BombBossScene.BombBoss import BombBoss
from app.scene.LevelSceneData import LevelSceneData
from app.sprites.LevelHUD import LevelHUD
from app.sprites.PlayerPlateform import PlayerPlateform
from ldLib.scene.SceneDataTMX import SceneDataTMX
from app.settings import *

class BombBossSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("BossRoom1", "InZone_01")
        self.sceneName = BOMB_BOSS_LEVEL
        self.nextLevel = INSTRUCTION_SCENE

        # Spawn boss
        for obj in self.tmxData.objects:
            if obj.name == "BossInZone":
                self.boss = BombBoss(obj.x, obj.y, self)
        self.allSprites.add(self.boss)
        self.enemyProjectiles.add(self.boss)
        self.allSprites.add(self.boss)
        self.camera.add(self.boss)
