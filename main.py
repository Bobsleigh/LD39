from app.SceneHandler import SceneHandler
from app.scene.SecondBossScene.SecondBossSceneData import SecondBossSceneData
from app.scene.SecondBossScene.SecondBossSceneLogicHandler import SecondBossSceneLogicHandler

import os
import sys

import pygame
from app.settings import *


if __name__ == '__main__':

    # Code to check if the code is running from a PyInstaller --onefile .exe
    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)

    # Screen
    screenSize = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screenSize)

    pygame.display.set_caption("A Thirst For Power")

    # Init
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.mixer.init()
    pygame.init()
    pygame.font.init()

    # Hide the mouse
    # pygame.mouse.set_visible(False)



    # Create the test scene
    sceneHandler = SceneHandler(screen)
    sceneHandler.mainLoop()