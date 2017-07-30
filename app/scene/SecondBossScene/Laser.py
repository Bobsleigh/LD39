import pygame, os

from app.scene.SecondBossScene import Boss2AI
from app.settings import *
from ldLib.collision.collisionMask import CollisionMask
from ldLib.tools.ImageBox import ImageBox
from ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from ldLib.Sprites.Player.IdleState import IdleState


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData, positionFromEnd = False, max_health=10):
        super().__init__()

        self.name = "Laser"

        tempImage = pygame.image.load(os.path.join('img', 'laser.png'))
        self.imageBase = pygame.transform.scale(tempImage, (600, 30))
        self.imageBase.set_colorkey(COLORKEY)

        self.imageShapeLeft = None
        self.imageShapeRight = None

        self.setShapeImage()
        self.image = self.imageShapeRight

        self.imageTransparent = ImageBox().rectSurface((32, 32), WHITE, 3)
        self.imageTransparent.set_colorkey(COLORKEY)

        self.rect = self.imageBase.get_rect()  # Position centrée du player
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.previousX = x
        self.previousY = y

        if positionFromEnd:
            self.x = x - self.rect.width
            x = self.x
            self.rect.x = x
            self.previousX = x

        self.speedx = 0
        self.speedy = 0
        self.maxSpeedx = 1
        self.maxSpeedyUp = 1
        self.maxSpeedyDown = 1
        self.accx = 1
        self.accy = 1
        self.jumpSpeed = 15
        self.springJumpSpeed = 25
        self.damage = 10

        self.isFrictionApplied = True
        self.isCollisionApplied = True
        self.facingSide = RIGHT
        self.friendly = True

        self.mapData = sceneData

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

    def setShapeImage(self):
        self.imageShapeLeft = pygame.transform.flip(self.imageBase, True, False)
        self.imageShapeRight = self.imageBase

    def rotate(self, degree):
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()  # Position centrée du player
        self.rect.x = self.x
        self.rect.y = self.y
        self.updateCollisionMask()

    def update(self):
        self.updateCollisionMask()

    def moveX(self):
        self.x += self.speedx
        self.collisionMask.rect.x = self.x

    def moveY(self):
        self.y += self.speedy
        self.collisionMask.rect.y = self.y

    def capSpeed(self):
        if self.speedx > 0 and self.speedx > self.maxSpeedx:
            self.speedx = self.maxSpeedx
        if self.speedx < 0 and self.speedx < -self.maxSpeedx:
            self.speedx = -self.maxSpeedx
        if self.speedy > 0 and self.speedy > self.maxSpeedyDown:
            self.speedy = self.maxSpeedyDown
        if self.speedy < 0 and self.speedy < -self.maxSpeedyUp:
            self.speedy = -self.maxSpeedyUp

    def updateSpeedRight(self):
        self.speedx += self.accx

    def updateSpeedLeft(self):
        self.speedx -= self.accx

    def updateSpeedUp(self):
        self.speedy -= self.accy

    def updateSpeedDown(self):
        self.speedy += self.accy

    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y

    def stop(self):
        self.speedx = 0
        self.speedy = 0