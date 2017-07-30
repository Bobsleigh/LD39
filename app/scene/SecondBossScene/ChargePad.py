import pygame, os, random

from app.settings import *
from ldLib.tools.Counter import Counter


class ChargePad(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData, max_health=10):
        super().__init__()

        self.name = "ChargePad"

        self.imageBase = pygame.image.load(os.path.join('img', 'charge-pad.png'))
        self.imageBase.set_colorkey(COLORKEY)

        self.imageShapeLeft = None
        self.imageShapeRight = None

        self.imageTransparent = pygame.Surface((1, 1),pygame.SRCALPHA)

        self.image = self.imageBase

        self.rect = self.image.get_rect()  # Position centrée du player
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.previousX = x
        self.previousY = y

        self.speedx = 0
        self.speedy = 0
        self.maxSpeedx = 1
        self.maxSpeedy = 1
        self.accx = 2
        self.accy = 2
        self.jumpSpeed = 15
        self.springJumpSpeed = 25

        self.isFrictionApplied = True
        self.isCollisionApplied = True
        self.facingSide = RIGHT
        self.friendly = True

        self.rightPressed = False
        self.leftPressed = False
        self.upPressed = False
        self.downPressed = False
        self.leftShiftPressed = False
        self.spacePressed = False
        self.leftMousePressed = False
        self.rightMousePressed = False

        self.sceneData = sceneData

        self.isAlive = True

        self.moveCounter = Counter()
        self.currentPosition = 0

    def update(self):
        self.moveCounter.count()

        if self.moveCounter.value == 500:
            self.move()
            self.moveCounter.reset()

    def move(self):
        rnd = random.randint(0, 5)
        if rnd != self.currentPosition:
            if rnd == 0:
                self.rect.x = 400
                self.rect.y = 250
            elif rnd == 1:
                self.rect.x = 100
                self.rect.y = 100
            elif rnd == 2:
                self.rect.x = 700
                self.rect.y = 100
            elif rnd == 3:
                self.rect.x = 600
                self.rect.y = 400
            elif rnd == 4:
                self.rect.x = 100
                self.rect.y = 500



