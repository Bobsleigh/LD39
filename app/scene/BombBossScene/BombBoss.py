import pygame
import os
import random
from app.settings import *
from ldLib.collision.collisionMask import CollisionMask
from ldLib.tools.ImageBox import ImageBox
from ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from ldLib.Sprites.Player.IdleState import IdleState
from app.scene.BombBossScene.BombBossAI import BombBossAI
from app.scene.BombBossScene.BoomBomb import BoomBomb
from app.scene.BombBossScene.ZapBomb import ZapBomb


class BombBoss(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData, max_health=10):
        super().__init__()

        self.name = "BombBoss"

        self.imageBase = pygame.image.load(os.path.join('img', 'canon-boss-closed.png'))
        self.imageBase.set_colorkey(COLORKEY)

        self.imageShapeLeft = None
        self.imageShapeRight = None

        self.setShapeImage()
        self.image = self.imageShapeRight

        self.imageTransparent = ImageBox().rectSurface((32, 32), WHITE, 3)
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
        self.maxSpeedx = 600
        self.maxSpeedyUp = 600
        self.maxSpeedyDown = 600
        self.accx = 1
        self.accy = 1
        self.jumpSpeed = 15
        self.springJumpSpeed = 25

        self.isFrictionApplied = False
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

        self.mapData = sceneData

        self.isAlive = True

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.collisionRules = []
        self.collisionRules.append(CollisionWithNothing())  # Gotta be first in the list to work properly
        self.collisionRules.append(CollisionWithSolid())

        self._state = IdleState()
        self.AI = BombBossAI(self, self.mapData)
        # self.nextState = None

    def setShapeImage(self):
        self.imageShapeLeft = pygame.transform.flip(self.imageBase, True, False)
        self.imageShapeRight = self.imageBase

    def update(self):
        self.AI.update()
        self.capSpeed()

        self.previousX = self.x
        self.previousY = self.y

        self.moveX()
        self.moveY()
        self.rect.x = self.x
        self.rect.y = self.y

        # Life bar
        self.maxHealth = 100
        self.currentHealth = 100

        if self.speedx > 0:
            self.image = self.imageShapeRight
            self.facingSide = RIGHT
        if self.speedx < 0:
            self.image = self.imageShapeLeft
            self.facingSide = LEFT

        self.updateCollisionMask()
        self.updatePressedKeys()

    def moveX(self):
        self.x += self.speedx
        self.collisionMask.rect.x = self.x
        for rule in self.collisionRules:
            rule.onMoveX(self)
        self.speedx *= 0.98

    def moveY(self):
        self.y += self.speedy
        self.collisionMask.rect.y = self.y
        for rule in self.collisionRules:
            rule.onMoveY(self)
        self.speedy *= 0.98

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

    def Boom(self):
        target_position = self.aim_for_player()
        desiredX = target_position[0]
        desiredY = target_position[1]

        boom_bomb = BoomBomb(desiredX, desiredY,self.rect.x, self.rect.y, self.mapData)
        self.mapData.allSprites.add(boom_bomb)
        self.mapData.camera.add(boom_bomb)
        print("I want to throw a BOOM bomb to " + str(desiredX) + "/" + str(desiredY))

    def Zap(self):
        zapBehaviors = ["aimForPlayer", "aimForPlates", "aimForEntrance"]
        chosenAction = random.choice(zapBehaviors)

        if chosenAction == "aimForPlayer":
            target_position = self.aim_for_player()
            desiredX = target_position[0] + random.randint(-32, 32)
            desiredY = target_position[1] + random.randint(-32, 32)

        elif chosenAction == "aimForPlates":
            desiredX = 390
            desiredY = 300

        else:
            desiredX = 390
            desiredY = 532

        zap_bomb = ZapBomb(desiredX, desiredY, self.rect.x, self.rect.y, self.mapData)
        self.mapData.allSprites.add(zap_bomb)
        self.mapData.camera.add(zap_bomb)
        print("I want to throw a ZAP bomb to " + str(desiredX) + "/" + str(desiredY))

    def Dash(self):

        self.speedx = (self.mapData.player.rect.x + 16 - self.rect.x)/20
        self.speedy = (self.mapData.player.rect.y + 16 - self.rect.y)/20

    def aim_for_player(self):
        target_position = [0, 0]
        target_position[0] = (self.mapData.player.rect.x + 16 + (20*self.mapData.player.speedx))
        target_position[1] = (self.mapData.player.rect.y + 32 + (20*self.mapData.player.speedy))

        if target_position[0] < 64:
            target_position[0] = 64
        elif target_position[0] > 732:
            target_position[0] = 732
        if target_position[1] < 64:
            target_position[1] = 64
        elif target_position[1] > 532:
            target_position[1] = 53

        return target_position

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

    # def notify(self, event):
    #     self.nextState = self.state.handleInput(self, event)

        # if self.nextState != None:
        #     self.state.exit(self)
        #     self.state = self.nextState
        #     self.state.enter(self)
        #     self.nextState = None

    # @property
    # def state(self):
    #     return self._state
    #
    # @state.setter
    # def state(self, value):
    #     self._state.exit(self)
    #     self._state = value
    #     self._state.enter(self)


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
            pass
        if self.rightMousePressed:
            pass
        if self.leftShiftPressed:
            pass
        if self.spacePressed:
            pass

    def jump(self):
        self.speedy = -self.jumpSpeed
