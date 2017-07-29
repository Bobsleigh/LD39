from app.scene.titleScene.CreditSceneData import CreditSceneData
from app.scene.titleScene.InstructionSceneData import InstructionSceneData
from app.scene.titleScene.TitleSceneData import TitleSceneData
from app.scene.titleScene.TitleSceneLogicHandler import TitleSceneLogicHandler
from app.settings import *
from app.scene.corridorScene.CorridorSceneData import CorridorSceneData
from app.scene.corridorScene.CorridorLevel1SceneData import CorridorLevel1SceneData
from app.scene.corridorScene.CorridorSceneLogicHandler import CorridorSceneLogicHandler

from app.scene.SecondBossScene.SecondBossSceneData import SecondBossSceneData
from app.scene.SecondBossScene.SecondBossSceneLogicHandler import SecondBossSceneLogicHandler

from app.scene.BombBossScene.BombBossSceneData import BombBossSceneData
from app.scene.BombBossScene.BombBossSceneLogicHandler import BombBossSceneLogicHandler

from ldLib.scene.GameData import GameData

from ldLib.scene.Scene import Scene
from app.settings import *


class SceneHandler:
    def __init__(self, screen):

        self.handlerRunning = True
        self.screen = screen
        self.gameData = GameData()

        if TAG_MAGNAN == 1:
            self.gameData.sceneData = BombBossSceneData()
            logic_handler = BombBossSceneLogicHandler(self.gameData)
            bomb_boss_scene = Scene(self.screen, self.gameData, logic_handler)
            bomb_boss_scene.run()

        elif TAG_PHIL == 1:
            self.gameData.sceneData = SecondBossSceneData()
            logicHandler = SecondBossSceneLogicHandler(self.gameData)
            secondBossScene = Scene(self.screen, self.gameData, logicHandler)
            secondBossScene.run()

        # elif TAG_MARIE == 1:
        #     self.gameData.sceneData = BombBossSceneData()
        #     logic_handler = BombBossSceneLogicHandler(self.gameData)
        #     bomb_boss_scene = Scene(self.screen, self.gameData, logic_handler)
        #     bomb_boss_scene.run()

        self.gameData.sceneData = TitleSceneData()
        self.runningScene = Scene(self.screen, self.gameData, TitleSceneLogicHandler(self.gameData))

    def mainLoop(self):
        self.handlerRunning = True
        while self.handlerRunning:
            self.getNextScene()
            self.runningScene.run()

    def getNextScene(self):
        # When we exit the scene, this code executes
        if self.runningScene.nextScene == TITLE_SCENE:
            self.gameData.sceneData = TitleSceneData()
            self.runningScene = Scene(self.screen, self.gameData, TitleSceneLogicHandler(self.gameData))
        elif self.runningScene.nextScene == INSTRUCTION_SCENE:
            self.gameData.sceneData = InstructionSceneData()
            self.runningScene = Scene(self.screen, self.gameData, TitleSceneLogicHandler(self.gameData))
        elif self.runningScene.nextScene == CREDIT_SCENE:
            self.gameData.sceneData = CreditSceneData()
            self.runningScene = Scene(self.screen, self.gameData, TitleSceneLogicHandler(self.gameData))
        elif self.runningScene.nextScene == TEST_TMX_SCENE:
            self.gameData.sceneData = CorridorSceneData()
            self.runningScene = Scene(self.screen, self.gameData, CorridorSceneLogicHandler(self.gameData))