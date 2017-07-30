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

        boxWidth = 0.7 * SCREEN_WIDTH
        self.createControlBox(SCREEN_WIDTH/2-boxWidth/2, 1*SCREEN_HEIGHT / 7, boxWidth,4 * SCREEN_HEIGHT / 7)

        buttonWidth = 0.55 * SCREEN_WIDTH-100
        self.backToTitleScreenButton = Button((SCREEN_WIDTH/2-buttonWidth/2, 16 * SCREEN_HEIGHT / 20), (buttonWidth, 50), 'Back to main menu',
                                              self.goToTitleScreen)
        self.spritesHUD.add(self.backToTitleScreenButton)
        self.notifyGroup.add(self.backToTitleScreenButton)

        self.musicName = "TitleScreen.wav"

    def createControlBox(self,x,y,width,height):
        self.textGoal = MessageBox(x,y,width,height)
        self.textGoal.textList.append('Play as the rebellious teen Lutecia')
        self.textGoal.textList.append('and free the world from the tyranny')
        self.textGoal.textList.append('of Superadmiral Kleido and his goons.')
        self.textGoal.textList.append('Make your way through his Fortress')
        self.textGoal.textList.append('of Power and take them down.')
        self.textGoal.textList.append('')
        self.textGoal.textList.append('CONTROLS:')
        self.textGoal.textList.append('Move with WASD.')
        self.textGoal.textList.append('Use your mouse to aim and shoot.')
        self.textGoal.textList.append('Stand on charging stations to charge.')
        # self.textGoal.textList.append('')
        # self.textGoal.textList.append('Press m to mute the game.')


        self.allSprites.add(self.textGoal)  # Add sprite

    def goToTitleScreen(self):
        self.nextScene = TITLE_SCENE


