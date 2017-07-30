from app.sprites.LevelHUD import LevelHUD
from app.sprites.PlayerPlateform import PlayerPlateform
from app.scene.GuardBossScene.GuardBoss import GuardBoss
from app.scene.LevelSceneData import LevelSceneData
from app.settings import *


class GuardBossSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("GuardBossRoom", "InZone_01")
        self.sceneName = GUARD_BOSS_LEVEL
        self.nextLevel = INSTRUCTION_SCENE

        # Spawn boss
        for obj in self.tmxData.objects:
            if obj.name == "BossInZone":
                self.boss = GuardBoss(obj.x, obj.y, self)
        self.allSprites.add(self.boss)
        self.enemyProjectiles.add(self.boss)
        self.allSprites.add(self.boss)
        self.camera.add(self.boss)
