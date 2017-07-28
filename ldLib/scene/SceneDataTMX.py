__author__ = 'Bobsleigh'
import logging
import os
import pygame
import pyscroll
import pytmx

from ldLib.scene.SceneData import SceneData
from app.settings import *

class SceneDataTMX(SceneData):
    def __init__(self, mapName="WorldMap", nameInZone="StartPointWorld", screenSize=(SCREEN_WIDTH,SCREEN_HEIGHT)):
        super().__init__()

        # Beginning MAP DATA
        self.nameMap = mapName

        # A set-up to shut down the logger 'orthographic' in pyscroll
        logger = logging.getLogger('orthographic')
        logger.setLevel(logging.ERROR)

        self.tmxData = pytmx.util_pygame.load_pygame(self.reqImageName(self.nameMap))
        self.tiledMapData = pyscroll.data.TiledMapData(self.tmxData)
        self.cameraPlayer = pyscroll.BufferedRenderer(self.tiledMapData, screenSize, clamp_camera=True)
        self.camera = pyscroll.PyscrollGroup(map_layer=self.cameraPlayer, default_layer=SPRITE_LAYER)

        # Spawn point of the player
        valBool = False
        for obj in self.tmxData.objects:
            if obj.name == "InZone":
                if obj.StartPoint == nameInZone:
                    self.spawmPointPlayerx = obj.x
                    self.spawmPointPlayery = obj.y

    def reqImageName(self, nameMap):
        return os.path.join('tiles_map', nameMap + ".tmx")