import pygame, os, random

from app.settings import *
from ldLib.animation.Animation import Animation


class ColaCan(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData, max_health=10):
        super().__init__()

        self.name = "ChargePad"

        self.frameAnimationSpeed = 15
        imageBase = pygame.image.load(os.path.join('img', 'unbranded-cola.png'))
        imageRot = pygame.transform.rotate(imageBase, 10)
        imageRot2 = pygame.transform.rotate(imageBase, 20)
        imageRot3 = pygame.transform.rotate(imageBase, -10)
        frames = [imageRot3,imageBase, imageRot,imageRot2,imageRot,imageBase]
        self.animation = Animation(frames, self.frameAnimationSpeed, True)
        self.image = frames[0]

        self.imageTransparent = pygame.Surface((1, 1),pygame.SRCALPHA)

        self.rect = self.image.get_rect()  # Position centrée du player
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

        self.sceneData = sceneData

    def update(self):
        # This sprite shouldn't be flipped.
        self.image = self.animation.update(LEFT)

