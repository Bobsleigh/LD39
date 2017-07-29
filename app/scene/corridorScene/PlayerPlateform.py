import os
import pygame
import math

from app.settings import *
from app.sprites.Bullet import PlayerBullet
from app.sprites.Target import Target

from ldLib.animation.Animation import Animation
from ldLib.collision.collisionMask import CollisionMask
from ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from ldLib.Sprites.Player.IdleState import IdleState
from ldLib.tools.Cooldown import Cooldown


class PlayerCorridor(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData):
        super().__init__()

        self.name = "player"

        # Code for idle animation
        frameAnimationSpeed=10

        imageIdle = [pygame.image.load(os.path.join('img', 'lutecia-left.png')),
                         pygame.image.load(os.path.join('img', 'lutecia-up.png'))]

        self.animationIdle = Animation(imageIdle, frameAnimationSpeed, LEFT, True)
        self.animation = self.animationIdle

        # Code for walking animation
        imageWalk = [pygame.image.load(os.path.join('img', 'lutecia-left-walk1.png')),
                         pygame.image.load(os.path.join('img', 'lutecia-left-walk2.png'))]
        self.animationWalk = Animation(imageWalk, frameAnimationSpeed, True)

        self.image = imageIdle[0]
        self.facingSide = RIGHT

        imageIdle

        self.imageTransparent = pygame.Surface((1, 1))
        self.imageTransparent.set_colorkey(COLORKEY)

        self.rect = self.image.get_rect()  # Position centrée du player
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.previousX = x
        self.previousY = y

        self.speedx = 0
        self.speedy = 0
        self.maxSpeedx = 3
        self.maxSpeedyUp = 3
        self.maxSpeedyDown = 3
        self.accx = 2
        self.accy = 2
        self.jumpSpeed = 15
        self.springJumpSpeed = 25

        self.isFrictionApplied = True
        self.isCollisionApplied = True
        self.friendly = True

        self.rightPressed = False
        self.leftPressed = False
        self.upPressed = False
        self.downPressed = False
        self.leftShiftPressed = False
        self.spacePressed = False
        self.leftMousePressed = False
        self.rightMousePressed = False

        self.mapData = sceneData

        self.isAlive = True

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.collisionRules = []
        self.collisionRules.append(CollisionWithNothing())  # Gotta be first in the list to work properly
        self.collisionRules.append(CollisionWithSolid())

        self._state = IdleState()
        # self.nextState = None

        # To shoot
        self.target = Target(0, 0)
        self.mapData.camera.add(self.target)

        self.gunCooldown = Cooldown(PLAYER_BULLET_COOLDOWN)

        self.soundShootGun = pygame.mixer.Sound(os.path.join('music', 'Laser_Shoot.wav'))
        self.soundShootGun.set_volume(.15)

    def update(self):
        self.capSpeed()

        self.previousX = self.x
        self.previousY = self.y

        self.moveX()
        self.moveY()
        self.rect.x = self.x
        self.rect.y = self.y

        if self.speedx > 0:
            self.facingSide = RIGHT
        elif self.speedx < 0:
            self.facingSide = LEFT

        if ((self.speedx!=0) or (self.speedy!=0)):
            self.animation = self.animationWalk
        else:
            self.animation = self.animationIdle

        self.image = self.animation.update(direction=self.facingSide)

        self.updateCollisionMask()
        self.updatePressedKeys()
        self.updateTarget()
        self.updateCooldowns()

    def moveX(self):
        self.x += self.speedx
        self.collisionMask.rect.x = self.x
        for rule in self.collisionRules:
            rule.onMoveX(self)

    def moveY(self):
        self.y += self.speedy
        self.collisionMask.rect.y = self.y
        for rule in self.collisionRules:
            rule.onMoveY(self)

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

    def dead(self):
        self.isAlive = False

    def onSpike(self):
        self.kill()

    def onCollision(self, collidedWith, sideOfCollision,limit=0):
        if collidedWith == SOLID:
            if sideOfCollision == RIGHT:
                #On colle le player sur le mur à droite
                self.x = self.previousX
                self.rect.x = self.x
                self.updateCollisionMask()
                self.speedx = 0
                self.rect.right += self.mapData.tmxData.tilewidth - (self.collisionMask.rect.right % self.mapData.tmxData.tilewidth) - 1
            if sideOfCollision == LEFT:
                self.x = self.previousX
                self.rect.x = self.x
                self.updateCollisionMask()
                self.speedx = 0
                self.rect.left -= (self.collisionMask.rect.left % self.mapData.tmxData.tilewidth)  # On colle le player sur le mur de gauche
            if sideOfCollision == DOWN:
                self.y = self.previousY
                self.rect.y = self.y
                self.updateCollisionMask()
                self.speedy = 0
            if sideOfCollision == UP:
                self.y = self.previousY
                self.rect.y = self.y
                self.updateCollisionMask()
                self.speedy = 0

    def notify(self, event):
        self.nextState = self.state.handleInput(self, event)

        # if self.nextState != None:
        #     self.state.exit(self)
        #     self.state = self.nextState
        #     self.state.enter(self)
        #     self.nextState = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state.exit(self)
        self._state = value
        self._state.enter(self)


    def updatePressedKeys(self):
        if self.rightPressed:
            self.updateSpeedRight()
        if self.leftPressed:
            self.updateSpeedLeft()
        if self.upPressed:
            self.updateSpeedUp()
        if self.downPressed:
            self.updateSpeedDown()
        if self.leftMousePressed:
            self.shootBullet()
        if self.rightMousePressed:
            pass
        if self.leftShiftPressed:
            pass
        if self.spacePressed:
            pass


    def updateTarget(self):
        mousePos = pygame.mouse.get_pos()

        diffx = mousePos[0] + self.mapData.cameraPlayer.view_rect.x - self.rect.centerx
        diffy = mousePos[1] + self.mapData.cameraPlayer.view_rect.y - self.rect.centery

        self.target.rect.centerx = TARGET_DISTANCE * (diffx) / self.vectorNorm(diffx, diffy) + self.rect.centerx
        self.target.rect.centery = TARGET_DISTANCE * (diffy) / self.vectorNorm(diffx, diffy) + self.rect.centery

        self.target.powerx = (diffx) / self.vectorNorm(diffx, diffy)
        self.target.powery = (diffy) / self.vectorNorm(diffx, diffy)

        angleRad = math.atan2(diffy, diffx)
        self.target.image = pygame.transform.rotate(self.target.imageOrig, -angleRad / math.pi * 180)


    def vectorNorm(self, x, y):
        return math.sqrt(x ** 2 + y ** 2 + EPS)

    def updateCooldowns(self):
        self.gunCooldown.update()

    def shootBullet(self):
        if self.gunCooldown.isZero:
            self.soundShootGun.play()

            bullet = PlayerBullet(self.rect.centerx, self.rect.centery, self.target.powerx*PLAYER_BULLET_SPEED, self.target.powery*PLAYER_BULLET_SPEED)
            self.mapData.camera.add(bullet)
            self.mapData.allSprites.add(bullet)
            self.gunCooldown.start()