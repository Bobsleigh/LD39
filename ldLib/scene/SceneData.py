__author__ = 'Bobsleigh'

import pygame
from ldLib.tools.NotifyGroup import NotifyGroup

class SceneData:
    def __init__(self):
        self.nextScene = None

        self.notifyGroup = NotifyGroup()
        self.allSprites = pygame.sprite.Group()
        self.friendlyBullets = pygame.sprite.Group()
        self.enemyProjectiles = pygame.sprite.Group()
        self.spritesHUD = pygame.sprite.Group()
        self.spritesBackGround = pygame.sprite.Group()

        self.player = None
        self.camera = None

        self.endSceneCause = None

    def beforeLeavingScene(self,screen):
        pass