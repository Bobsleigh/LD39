import pygame

class LogicHandler:
    def __init__(self,gameData):
        self.gameData = gameData
        self.sceneData = gameData.sceneData
        self.nextScene = None

    def handle(self):
        self.sceneData.allSprites.update()
        self.sceneData.spritesHUD.update()
        self.sceneData.spritesBackGround.update()