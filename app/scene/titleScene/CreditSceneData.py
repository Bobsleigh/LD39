
import pygame
import os

from ldLib.GUI.Button import Button
from ldLib.GUI.messageBox.MessageBox import MessageBox

from app.settings import *

import weakref

from ldLib.scene.SceneData import SceneData


class CreditSceneData(SceneData):
    def __init__(self):
        super().__init__()

        # background
        self.background = pygame.sprite.Sprite()
        self.background.rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.background.image = pygame.image.load(os.path.join('img', 'menu.png'))
        self.background.rect = self.background.image.get_rect()

        self.spritesBackGround.add(self.background)

        self.player = None
        self.camera = None

        widthCreditBox = 0.5*SCREEN_WIDTH
        heightCreditBox = 0.6*SCREEN_HEIGHT

        self.createCreditBox(SCREEN_WIDTH/2-widthCreditBox/2, 1*SCREEN_HEIGHT / 7, widthCreditBox, heightCreditBox)

        buttonWidth = 0.55 * SCREEN_WIDTH - 100
        self.backToTitleScreenButton = Button((SCREEN_WIDTH / 2 - buttonWidth / 2, 16 * SCREEN_HEIGHT / 20),
                                              (buttonWidth, 50), 'Back to main menu',
                                              self.goToTitleScreen)

        self.spritesHUD.add(self.backToTitleScreenButton)
        self.notifyGroup.add(self.backToTitleScreenButton)

    def createCreditBox(self,x,y,width,height):
        self.textGoal = MessageBox(x,y,width,height,fontSize=12)
        self.textGoal.textList.append('Game made for the Ludum Dare 39')
        # self.textGoal.textList.append('')
        self.textGoal.textList.append('July 28-30 2017')
        self.textGoal.textList.append('')
        self.textGoal.textList.append('Gameplay, Design, and Graphics by:')
        # Removed reference to music because we didn't deal with that
        self.textGoal.textList.append('')
        self.textGoal.textList.append('The Bobsleigh team')
        self.textGoal.textList.append('')

        self.allSprites.add(self.textGoal)  # Add sprite

    def goToTitleScreen(self):
        self.nextScene = TITLE_SCENE