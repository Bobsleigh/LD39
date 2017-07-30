import pygame
import os
import random
import math
from app.settings import *
from ldLib.animation.Animation import Animation
from ldLib.collision.collisionMask import CollisionMask
from ldLib.tools.ImageBox import ImageBox
from ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from ldLib.Sprites.Player.IdleState import IdleState
from ldLib.tools.Cooldown import Cooldown
from app.scene.BombBossScene.BombBossAI import BombBossAI
from app.scene.BombBossScene.BoomBomb import BoomBomb
from app.scene.BombBossScene.ZapBomb import ZapBomb


class BombBoss(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData, max_health=10):
        super().__init__()

        self.name = "Dreetus: Demolition Expert"

        # Animation
        self.frameAnimationSpeed = 10
        imageBase = pygame.image.load(os.path.join('img', 'canon-boss-closed.png'))
        imageOpen = pygame.image.load(os.path.join('img', 'canon-boss-open.png'))
        imageDashAnim1 = pygame.image.load(os.path.join('img', 'canon-boss-dash1.png'))
        imageDashAnim2 = pygame.image.load(os.path.join('img', 'canon-boss-dash2.png'))

        self.imageIdle = [imageBase, imageBase,
                          imageBase, imageBase,
                          imageBase, imageBase,
                          imageOpen, imageOpen,
                          imageBase, imageBase,
                          imageBase, imageBase,
                          imageOpen, imageOpen]
        self.animationIdle = Animation(self.imageIdle, self.frameAnimationSpeed, RIGHT, True)
        imageDash = [imageDashAnim1,imageDashAnim2]
        self.animationDash = Animation(imageDash, self.frameAnimationSpeed, RIGHT, True)
        self.animation = self.animationIdle
        self.image = self.imageIdle[0]
        self.facingSide = RIGHT

        self.imageTransparent = pygame.Surface((1, 1), pygame.SRCALPHA)

        self.rect = self.image.get_rect()  # Position centrée du player
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.previousX = x
        self.previousY = y

        self.speedx = 0
        self.speedy = 0
        self.accx = 1
        self.accy = 1
        self.jumpSpeed = 15
        self.springJumpSpeed = 25

        self.isFrictionApplied = False
        self.isCollisionApplied = True
        self.facingSide = RIGHT
        self.friendly = True

        # Life bar
        self.maxHealth = 1500
        self.currentHealth = 1500

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

        # For invincibility
        self.invincibleCooldown = Cooldown(BOSS_INVINCIBILITY_COOLDOWN)
        self.flashduration = 8

        self.hurtSound = pygame.mixer.Sound(os.path.join('music', 'Hit_Hurt.wav'))
        self.hurtSound.set_volume(.25)

    def update(self):
        self.AI.update()

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

        self.image = self.animation.update(self.facingSide)

        # Replace to make visual flash in invincible mode.
        if not self.invincibleCooldown.isZero:
            if self.flashduration - 3 <= self.invincibleCooldown.value % self.flashduration:
                self.image = self.imageTransparent

        self.updateCollisionMask()
        self.updatePressedKeys()
        self.updateCooldowns()

    def moveX(self):
        self.x += self.speedx
        self.collisionMask.rect.x = self.x
        for rule in self.collisionRules:
            rule.onMoveX(self)
        self.speedx *= 0.97

    def moveY(self):
        self.y += self.speedy
        self.collisionMask.rect.y = self.y
        for rule in self.collisionRules:
            rule.onMoveY(self)
        self.speedy *= 0.97

    def hurt(self, damage):
        if self.invincibleCooldown.isZero:
            self.currentHealth -= damage
            self.checkIfIsAlive()
            self.invincibleOnHit()

    def checkIfIsAlive(self):
        if self.currentHealth <= 0:
            self.dead()

    def invincibleOnHit(self):
        self.invincibleCooldown.start()

    def updateCooldowns(self):
        # For invincibility
        self.invincibleCooldown.update()

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
        self.mapData.BombBossIsDead()
        self.isAlive = False
        self.kill()

    def Boom(self):
        target_position = self.aim_for_player()
        desiredX = target_position[0]
        desiredY = target_position[1]

        boom_bomb = BoomBomb(desiredX, desiredY, self.rect.x, self.rect.y, self.mapData)
        self.mapData.allSprites.add(boom_bomb)
        self.mapData.camera.add(boom_bomb)

    def boomOnPlate(self):
        boom_bomb = BoomBomb(390, 300, self.rect.x, self.rect.y, self.mapData)
        self.mapData.allSprites.add(boom_bomb)
        self.mapData.camera.add(boom_bomb)

    def Zap(self):
        zapBehaviors = ["aimForPlayer"] * 5 + ["aimForPlates"] * 2 + ["aimForEntrance"]*3
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

    def prettyZap(self, pattern_id):
        if pattern_id == 1:
            zap_bomb_1 = ZapBomb(390, 120, self.rect.x, self.rect.y, self.mapData)
            zap_bomb_2 = ZapBomb(201, 420, self.rect.x, self.rect.y, self.mapData)
            zap_bomb_3 = ZapBomb(610, 420, self.rect.x, self.rect.y, self.mapData)
            self.mapData.allSprites.add(zap_bomb_3)
            self.mapData.camera.add(zap_bomb_3)
        elif pattern_id == 2:
            zap_bomb_1 = ZapBomb(395, 420, self.rect.x, self.rect.y, self.mapData)
            zap_bomb_2 = ZapBomb(201, 120, self.rect.x, self.rect.y, self.mapData)
            zap_bomb_3 = ZapBomb(610, 120, self.rect.x, self.rect.y, self.mapData)
            self.mapData.allSprites.add(zap_bomb_3)
            self.mapData.camera.add(zap_bomb_3)
        else:
            zap_bomb_1 = ZapBomb(600, 300, self.rect.x, self.rect.y, self.mapData)
            zap_bomb_2 = ZapBomb(200, 300, self.rect.x, self.rect.y, self.mapData)
        self.mapData.allSprites.add(zap_bomb_1)
        self.mapData.camera.add(zap_bomb_1)
        self.mapData.allSprites.add(zap_bomb_2)
        self.mapData.camera.add(zap_bomb_2)

    def smallDash(self):
        x = self.mapData.player.rect.centerx - self.rect.centerx
        y = self.mapData.player.rect.centery - self.rect.centery
        angle = math.atan2(y, x)

        self.speedx = 3 * math.cos(angle)
        self.speedy = 3 * math.sin(angle)

    def Dash(self):
        x = self.mapData.player.rect.centerx - self.rect.centerx
        y = self.mapData.player.rect.centery - self.rect.centery
        angle = math.atan2(y, x)

        self.speedx = 7 * math.cos(angle)
        self.speedy = 7 * math.sin(angle)

    def aim_for_player(self):
        target_position = [0, 0]
        target_position[0] = (self.mapData.player.rect.x + 16 + (20 * self.mapData.player.speedx))
        target_position[1] = (self.mapData.player.rect.y + 32 + (20 * self.mapData.player.speedy))

        if target_position[0] < 64:
            target_position[0] = 64
        elif target_position[0] > 732:
            target_position[0] = 732
        if target_position[1] < 64:
            target_position[1] = 64
        elif target_position[1] > 532:
            target_position[1] = 532

        return target_position

    def onCollision(self, collidedWith, sideOfCollision, limit=0):
        if collidedWith == SOLID:
            if sideOfCollision == RIGHT:
                # On colle le player sur le mur à droite
                self.x = self.previousX
                self.rect.x = self.x
                self.updateCollisionMask()
                self.speedx = 0
                self.rect.right += self.mapData.tmxData.tilewidth - (
                    self.collisionMask.rect.right % self.mapData.tmxData.tilewidth) - 1
            if sideOfCollision == LEFT:
                self.x = self.previousX
                self.rect.x = self.x
                self.updateCollisionMask()
                self.speedx = 0
                self.rect.left -= (
                    self.collisionMask.rect.left % self.mapData.tmxData.tilewidth)  # On colle le player sur le mur de gauche
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
