import pygame, os
from app.scene.BombBossScene.BombBossSceneData import BombBossSceneData
from app.scene.BombBossScene.BombBossSceneLogicHandler import BombBossSceneLogicHandler
from app.scene.GuardBossScene.GuardBossSceneData import GuardBossSceneData
from app.scene.GuardBossScene.GuardBossSceneLogicHandler import GuardBossSceneLogicHandler
from app.scene.SecondBossScene.SecondBossSceneData import SecondBossSceneData
from app.scene.SecondBossScene.SecondBossSceneLogicHandler import SecondBossSceneLogicHandler
from app.scene.corridorScene.CorridorGuardSceneData import CorridorGuardSceneData
from app.scene.corridorScene.CorridorBombSceneData import CorridorBombSceneData
from app.scene.corridorScene.CorridorLaserSceneData import CorridorLaserSceneData
from app.scene.corridorScene.CorridorSceneData import CorridorSceneData
from app.scene.corridorScene.CorridorSceneLogicHandler import CorridorSceneLogicHandler
from app.scene.titleScene.CreditSceneData import CreditSceneData
from app.scene.titleScene.EndingSceneData import EndingSceneData
from app.scene.titleScene.InstructionSceneData import InstructionSceneData
from app.scene.titleScene.TitleSceneData import TitleSceneData
from app.scene.titleScene.TitleSceneLogicHandler import TitleSceneLogicHandler
from app.settings import *
from ldLib.scene.GameData import GameData
from ldLib.scene.MusicHandler import MusicHandler
from ldLib.scene.Scene import Scene


class SceneHandler:
    def __init__(self, screen):

        self.handlerRunning = True
        self.screen = screen
        self.gameData = GameData()

        self.gameData.sceneData = TitleSceneData()
        self.runningScene = Scene(self.screen, self.gameData, TitleSceneLogicHandler(self.gameData), MusicHandler(self.gameData))

        if TAG_MAGNAN == 1:
            self.gameData.sceneData = GuardBossSceneData()
            logic_handler = GuardBossSceneLogicHandler(self.gameData)
            self.runningScene = Scene(self.screen, self.gameData, logic_handler)

        # elif TAG_PHIL == 1:
        #     self.gameData.sceneData = SecondBossSceneData()
        #     self.runningScene = Scene(self.screen, self.gameData, SecondBossSceneLogicHandler(self.gameData), MusicHandler(self.gameData))

        # pygame.mixer.music.load(os.path.join('music', "TitleScreen.wav"))
        # pygame.mixer.music.set_volume(1.0)
        # pygame.mixer.music.play(-1)

        # elif TAG_MARIE == 1:
        #     self.gameData.sceneData = BombBossSceneData()
        #     logic_handler = BombBossSceneLogicHandler(self.gameData)
        #     self.runningScene = Scene(self.screen, self.gameData, logic_handler)

    def mainLoop(self):
        self.handlerRunning = True
        while self.handlerRunning:
            self.getNextScene()
            self.runningScene.run()

    def getNextScene(self):
        # When we exit the scene, this code executes
        if self.runningScene.nextScene == TITLE_SCENE:
            self.gameData.sceneData = TitleSceneData()
            self.runningScene = Scene(self.screen, self.gameData, TitleSceneLogicHandler(self.gameData), MusicHandler(self.gameData))
        elif self.runningScene.nextScene == INSTRUCTION_SCENE:
            self.gameData.sceneData = InstructionSceneData()
            self.runningScene = Scene(self.screen, self.gameData, TitleSceneLogicHandler(self.gameData), MusicHandler(self.gameData))
        elif self.runningScene.nextScene == CREDIT_SCENE:
            self.gameData.sceneData = CreditSceneData()
            self.runningScene = Scene(self.screen, self.gameData, TitleSceneLogicHandler(self.gameData), MusicHandler(self.gameData))
        elif self.runningScene.nextScene == TEST_TMX_SCENE:
            self.gameData.sceneData = CorridorSceneData()
            self.runningScene = Scene(self.screen, self.gameData, CorridorSceneLogicHandler(self.gameData))
        elif self.runningScene.nextScene == GUARD_CORRIDOR_LEVEL:
            self.gameData.sceneData = CorridorGuardSceneData()
            self.runningScene = Scene(self.screen, self.gameData, CorridorSceneLogicHandler(self.gameData), MusicHandler(self.gameData))
        elif self.runningScene.nextScene == GUARD_BOSS_LEVEL:
            self.gameData.sceneData = GuardBossSceneData()
            self.runningScene = Scene(self.screen, self.gameData, GuardBossSceneLogicHandler(self.gameData), MusicHandler(self.gameData))
        elif self.runningScene.nextScene == BOMB_CORRIDOR_LEVEL:
            self.gameData.sceneData = CorridorBombSceneData()
            self.runningScene = Scene(self.screen, self.gameData, CorridorSceneLogicHandler(self.gameData), MusicHandler(self.gameData))
        elif self.runningScene.nextScene == BOMB_BOSS_LEVEL:
            self.gameData.sceneData = BombBossSceneData()
            self.runningScene = Scene(self.screen, self.gameData, BombBossSceneLogicHandler(self.gameData), MusicHandler(self.gameData))
        elif self.runningScene.nextScene == LASER_CORRIDOR_LEVEL:
            self.gameData.sceneData = CorridorLaserSceneData()
            self.runningScene = Scene(self.screen, self.gameData, CorridorSceneLogicHandler(self.gameData), MusicHandler(self.gameData))
        elif self.runningScene.nextScene == LASER_BOSS_LEVEL:
            self.gameData.sceneData = SecondBossSceneData()
            self.runningScene = Scene(self.screen, self.gameData, SecondBossSceneLogicHandler(self.gameData), MusicHandler(self.gameData))
        elif self.runningScene.nextScene == ENDING_SCENE:
            self.gameData.sceneData = EndingSceneData()
            self.runningScene = Scene(self.screen, self.gameData, TitleSceneLogicHandler(self.gameData), MusicHandler(self.gameData))