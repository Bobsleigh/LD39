import pygame

from ldLib.scene.EventHandler import EventHandler
from ldLib.scene.Drawer import Drawer
from app.settings import *


class Scene:
    def __init__(self,screen,gameData,logicHandler):
        # Screen
        self.gameData = gameData
        self.nextScene = None

        self.screen = screen
        self.sceneData = self.gameData.sceneData
        self.player = self.gameData.sceneData.player

        if self.player != None:
            self.sceneData.allSprites.add(self.player)
            self.sceneData.notifyGroup.add(self.player)

        if self.sceneData.camera != None:
            self.camera = self.sceneData.camera
            if self.player != None:
                self.sceneData.camera.add(self.player)
        else:
            self.camera = None

        self.eventHandler = EventHandler()
        self.logicHandler = logicHandler
        self.drawer = Drawer()

    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandler.eventHandle(self.sceneData.notifyGroup)
            self.logicHandler.handle()
            if self.sceneData.camera == None:
                self.drawer.draw(self.screen, self.sceneData.allSprites, self.sceneData.spritesHUD, self.sceneData.spritesBackGround, self.player)
            else:
                self.drawer.draw(self.screen, self.sceneData.camera, self.sceneData.spritesHUD, self.sceneData.spritesBackGround, self.player)
            self.nextScene = self.sceneData.nextScene

            if self.nextScene != None:
                self.sceneRunning = False
        self.sceneData.beforeLeavingScene(self.screen)

    def run(self):
        self.mainLoop()
