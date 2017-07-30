import pygame, os

from app.scene.BombBossScene.BombBoss import BombBoss
from app.scene.LevelSceneData import LevelSceneData
from app.settings import *
from app.scene.PlayerDeadFadeOut import PlayerDeadFadeOut
from app.scene.BossDeadFadeOut import BossDeadFadeOut


class BombBossSceneData(LevelSceneData):
    def __init__(self):
        super().__init__("BossRoom1", "InZone_01")
        self.sceneName = BOMB_BOSS_LEVEL
        self.nextLevel = LASER_CORRIDOR_LEVEL

        self.boss = None
        # Spawn boss
        for obj in self.tmxData.objects:
            if obj.name == "BossInZone":
                self.boss = BombBoss(obj.x, obj.y, self)
        self.allSprites.add(self.boss)
        self.enemyProjectiles.add(self.boss)
        self.allSprites.add(self.boss)
        self.camera.add(self.boss)
        self.addHUD()

        self.musicName = "BoxCat_Games_-_25_-_Victory.wav"

        self.boomBombSound = pygame.mixer.Sound(os.path.join('music', 'BoomBombExplosion.wav'))
        self.boomBombSound.set_volume(.8)

    def BombBossIsDead(self):
        self.nextScene = self.nextLevel
        self.endSceneCause = BOSS_DEAD

    def beforeLeavingScene(self, screen):
        if self.endSceneCause == BOSS_DEAD:
            BossDeadFadeOut(screen)

        if self.endSceneCause == PLAYER_DEAD:
            PlayerDeadFadeOut(screen)