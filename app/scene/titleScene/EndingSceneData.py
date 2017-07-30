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
        self.textGoal.textList.append('Congrats, you did it!')
        self.textGoal.textList.append("You beat Superadmiral Kleido and")
        self.textGoal.textList.append("restored peace! Now it's time to")
        self.textGoal.textList.append('go home and enjoy the fresh taste')
        self.textGoal.textList.append('of unbranded cola.')
        self.textGoal.textList.append('')
        self.textGoal.textList.append('Go ahead, you deserve it.')
        # self.textGoal.textList.append('')
        # self.textGoal.textList.append('Press m to mute the game.')


        self.allSprites.add(self.textGoal)  # Add sprite

    def goToTitleScreen(self):
        self.nextScene = TITLE_SCENE


