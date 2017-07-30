from app.scene.GuardBossScene.GuardBoss import GuardBoss
from app.scene.LevelSceneData import LevelSceneData
from app.settings import *
from app.scene.PlayerDeadFadeOut import PlayerDeadFadeOut
from app.scene.BossDeadFadeOut import BossDeadFadeOut


class GuardBossSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("GuardBossRoom", "InZone_01")
        self.sceneName = GUARD_BOSS_LEVEL
        self.nextLevel = BOMB_CORRIDOR_LEVEL

        self.boss = None
        # Spawn boss
        for obj in self.tmxData.objects:
            if obj.name == "BossInZone":
                self.boss = GuardBoss(obj.x, obj.y, self)
        self.allSprites.add(self.boss)
        self.enemyProjectiles.add(self.boss)
        self.allSprites.add(self.boss)
        self.camera.add(self.boss)
        self.addHUD()

    def GuardBossIsDead(self):
        self.nextScene = self.nextLevel
        self.endSceneCause = BOSS_DEAD

    def beforeLeavingScene(self, screen):
        if self.endSceneCause == BOSS_DEAD:
            BossDeadFadeOut(screen)

        if self.endSceneCause == PLAYER_DEAD:
            PlayerDeadFadeOut(screen)
