import pygame
import os

from ldLib.GUI.Button import Button
from ldLib.GUI.messageBox.MessageBox import MessageBox

from app.settings import *

import weakref

from ldLib.scene.SceneData import SceneData


class InstructionSceneData(SceneData):
    def __init__(self):
        super().__init__()

        # background
        self.background = pygame.sprite.Sprite()
        self.background.rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.background.image = pygame.image.load(os.path.join('img', 'menu.png'))
        self.background.rect = self.background.image.get_rect()

        self.spritesBackGround.add(self.background)

        boxWidth = 0.55 * SCREEN_WIDTH
        self.createControlBox(SCREEN_WIDTH/2-boxWidth/2, 3*SCREEN_HEIGHT / 7, boxWidth,3 * SCREEN_HEIGHT / 7)

        buttonWidth = 0.55 * SCREEN_WIDTH-100
        self.backToTitleScreenButton = Button((SCREEN_WIDTH/2-buttonWidth/2, 17 * SCREEN_HEIGHT / 20+20), (buttonWidth, 50), 'Back to main menu',
                                              self.goToTitleScreen)
        self.spritesHUD.add(self.backToTitleScreenButton)
        self.notifyGroup.add(self.backToTitleScreenButton)

    def createControlBox(self,x,y,width,height):
        self.textGoal = MessageBox(x,y,width,height)
        self.textGoal.textList.append('Free the country from the tyranny')
        self.textGoal.textList.append('of Superadmiral Kleido.')
        self.textGoal.textList.append('Make your way through the Starred Fortress')
        self.textGoal.textList.append('to take down the power.')
        self.textGoal.textList.append('')
        self.textGoal.textList.append('Move with WASD.')
        self.textGoal.textList.append('Use your mouse to aim and shoot.')
        self.textGoal.textList.append('Stand on charging stations to charge your gun.')
        # self.textGoal.textList.append('')
        # self.textGoal.textList.append('Press m to mute the game.')


        self.allSprites.add(self.textGoal)  # Add sprite

    def goToTitleScreen(self):
        self.nextScene = TITLE_SCENE


