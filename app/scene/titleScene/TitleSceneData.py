# Imports
import os
import sys

import pygame

from ldLib.GUI.Button import Button
from app.settings import *

import weakref

from ldLib.scene.SceneData import SceneData


class TitleSceneData(SceneData):
    def __init__(self):
        super().__init__()
        self.nextScene = None

        # background
        self.background = pygame.sprite.Sprite()
        self.background.rect = pygame.Rect(0,0,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.background.image = pygame.image.load(os.path.join('img', 'menu.png'))
        self.background.rect = self.background.image.get_rect()

        self.spritesBackGround.add(self.background)

        self.createStartMenu()

    def createStartMenu(self):
        buttonWidth = 300
        buttonHeight = 50
        self.startGameButton = Button((SCREEN_WIDTH/2-buttonWidth/2, 10 * SCREEN_HEIGHT / 20), (buttonWidth, buttonHeight), 'Start game',
                                       self.startGame)
        self.spritesHUD.add(self.startGameButton)
        self.notifyGroup.add(self.startGameButton)

        self.instructionButton = Button((SCREEN_WIDTH/2-buttonWidth/2, 12 * SCREEN_HEIGHT / 20), (buttonWidth, buttonHeight), 'Instructions',
                                      self.goToInstruction)
        self.spritesHUD.add(self.instructionButton)
        self.notifyGroup.add(self.instructionButton)

        self.creditButton = Button((SCREEN_WIDTH/2-buttonWidth/2, 14 * SCREEN_HEIGHT / 20), (buttonWidth, buttonHeight), 'Credit',
                                      self.goToCredit)
        self.spritesHUD.add(self.creditButton)
        self.notifyGroup.add(self.creditButton)

        self.exitButton = Button((SCREEN_WIDTH/2-buttonWidth/2, 16 * SCREEN_HEIGHT / 20), (buttonWidth, buttonHeight), 'Exit', sys.exit)
        self.spritesHUD.add(self.exitButton)
        self.notifyGroup.add(self.exitButton)

    def startGame(self):
        self.nextScene = BOMB_CORRIDOR_LEVEL

        if TAG_MARIE ==1:
            self.nextScene = GUARD_BOSS_LEVEL

    def goToInstruction(self):
        self.nextScene = INSTRUCTION_SCENE

    def goToCredit(self):
        self.nextScene = CREDIT_SCENE
