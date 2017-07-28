import os
import sys

import pygame

from app.scene.sceneHandler import SceneHandler
from app.scene.titleScreen.titleScreen import TitleScreen
from app.settings import *

if __name__ == '__main__':

    # Uncomment the test you want to run. This main file is needed to keep the relative path intact.

    exec(open('FeatureTests\TileCollisions\Test.py').read())
    #exec(open('FeatureTests\DialogBox\Test.py').read())