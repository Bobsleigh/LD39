from app.settings import *
from app.scene.corridorScene.CorridorSceneData import CorridorSceneData
from app.scene.corridorScene.CorridorLevel1SceneData import CorridorLevel1SceneData
from app.scene.corridorScene.CorridorSceneLogicHandler import CorridorSceneLogicHandler

from ldLib.scene.GameData import GameData

from ldLib.scene.Scene import Scene
from app.settings import *


class SceneHandler:
    def __init__(self, screen):

        self.handlerRunning = True
        self.screen = screen
        self.gameData = GameData()

        self.gameData.sceneData = CorridorSceneData()
        self.runningScene = Scene(self.screen, self.gameData, CorridorSceneLogicHandler(self.gameData))

    def mainLoop(self):
        self.handlerRunning = True
        while self.handlerRunning:
            self.getNextScene()
            self.runningScene.run()

    def getNextScene(self):
        # When we exit the scene, this code executes
        if self.runningScene.nextScene == TITLE_SCENE:
            self.gameData.sceneData = CorridorSceneData()
            self.runningScene = Scene(self.screen, self.gameData, CorridorSceneLogicHandler(self.gameData))
        # elif self.runningScene.nextScene == INSTRUCTION_SCENE:
        #     self.gameData.data = InstructionSceneData()
        #     self.runningScene = Scene(self.screen, self.gameData, TitleSceneLogicHandler(self.gameData))
        # elif self.runningScene.nextScene == CREDIT_SCENE:
        #     self.gameData.data = CreditSceneData()
        #     self.runningScene = Scene(self.screen, self.gameData, TitleSceneLogicHandler(self.gameData))
        elif self.runningScene.nextScene == CORRIDOR_LEVEL_1:
            self.gameData.sceneData = CorridorLevel1SceneData()
            self.runningScene = Scene(self.screen, self.gameData, CorridorSceneLogicHandler(self.gameData))