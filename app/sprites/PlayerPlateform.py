import os
import pygame
import math

from app.settings import *
from app.sprites.Bullet import PlayerBullet
from app.sprites.Target import Target

from ldLib.animation.Animation import Animation
from ldLib.collision.CollisionRules.CollisionWithEnergyCharge import CollisionWithEnergyCharge
from ldLib.collision.collisionMask import CollisionMask
from ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from ldLib.Sprites.Player.IdleState import IdleState
from ldLib.tools.Cooldown import Cooldown


class PlayerPlateform(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData):
        super().__init__()

        self.name = "player"

        # Code for idle animation
        self.animationState = ANIMATION_NORMAL
        self.frameAnimationSpeed=10

        self.imageIdle = [pygame.image.load(os.path.join('img', 'lutecia-left.png'))]

        self.animationIdle = Animation(self.imageIdle, self.frameAnimationSpeed, LEFT, True)
        self.animation = self.animationIdle

        # Code for walking animation
        self.imageWalk = [pygame.image.load(os.path.join('img', 'lutecia-left-walk1.png')),
                         pygame.image.load(os.path.join('img', 'lutecia-left-walk2.png'))]
        self.animationWalk = Animation(self.imageWalk, self.frameAnimationSpeed, True)

        # Code for healthless animation
        self.imageIdleHealthless = [
            pygame.image.load(os.path.join('img\weak-lutecia\healthless', 'lutecia-left-healthless.png')),
            pygame.image.load(
                os.path.join('img\weak-lutecia\healthless', 'lutecia-left-healthless2.png'))]

        self.imageWalkHealthless = [
            pygame.image.load(os.path.join('img\weak-lutecia\healthless', 'lutecia-left-walk1-healthless.png')),
            pygame.image.load(
                os.path.join('img\weak-lutecia\healthless', 'lutecia-left-walk2-healthless.png'))]

        # Code for powerless animation
        self.imageIdlePowerless = [
            pygame.image.load(os.path.join('img\weak-lutecia', 'lutecia-left-powerless1.png')),
            pygame.image.load(
                os.path.join('img\weak-lutecia', 'lutecia-left-powerless2.png'))]

        self.imageWalkPowerless = [
            pygame.image.load(os.path.join('img\weak-lutecia', 'lutecia-left-walk-powerless1.png')),
            pygame.image.load(
                os.path.join('img\weak-lutecia', 'lutecia-left-walk-powerless2.png'))]

        # Code for healthless/powerless animation
        self.imageIdleHealthPowerless = [
            pygame.image.load(os.path.join('img\weak-lutecia\healthless', 'lutecia-left-healthless.png')),
            pygame.image.load(
                os.path.join('img\weak-lutecia\healthless', 'lutecia-left-powerless-healthless.png'))]

        self.imageWalkHealthPowerless = [
            pygame.image.load(os.path.join('img\weak-lutecia\healthless', 'lutecia-left-walk1-healthless.png')),
            pygame.image.load(
                os.path.join('img\weak-lutecia\healthless', 'lutecia-left-walk2-healthless-powerless.png'))]

        self.image = self.imageIdle[0]
        self.facingSide = RIGHT

        self.imageTransparent = pygame.Surface((1, 1),pygame.SRCALPHA)

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
        self.collisionRules.append(CollisionWithEnergyCharge())

        self._state = IdleState()
        # self.nextState = None

        # To shoot
        self.target = Target(0, 0)
        self.mapData.camera.add(self.target)
        self.gunCooldown = Cooldown(PLAYER_BULLET_COOLDOWN)

        self.soundShootGun = pygame.mixer.Sound(os.path.join('music', 'Laser_Shoot.wav'))
        self.soundShootGun.set_volume(.15)

        self.maxEnergy = PLAYER_MAX_ENERGY
        self.currentEnergy = self.maxEnergy
        self.rechargeCooldown = Cooldown(PLAYER_RECHARGE_COOLDOWN)

        # Life bar
        self.maxHealth = PLAYER_MAX_LIFE
        self.currentHealth = self.maxHealth

        self.hurtSound = pygame.mixer.Sound(os.path.join('music', 'Hit_Hurt.wav'))
        self.hurtSound.set_volume(.25)

        self.invincibleCooldown = Cooldown(60)
        self.flashduration = 8


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

        self.selectAnimation()

        if ((self.speedx!=0) or (self.speedy!=0)):
            self.animation = self.animationWalk
        else:
            self.animation = self.animationIdle

        if self.target.rect.centerx<self.rect.centerx:
            targetSide = LEFT
        else:
            targetSide=RIGHT
        self.image = self.animation.update(targetSide)

        # Replace to make visual flash in invincible mode.
        if not self.invincibleCooldown.isZero:
            if self.flashduration-3 <= self.invincibleCooldown.value % self.flashduration:
                self.image = self.imageTransparent

        self.updateCollisionMask()
        self.updatePressedKeys()
        self.updateTarget()
        self.updateCooldowns()

    def selectAnimation(self):
        if self.currentHealth < self.maxHealth / 3 and self.currentEnergy < self.maxEnergy / 3:
            if self.animationState is not ANIMATION_HEALTHLESS_POWERLESS:
                self.animationIdle = Animation(self.imageIdleHealthPowerless, self.frameAnimationSpeed, LEFT, True)
                self.animationWalk = Animation(self.imageWalkHealthPowerless, self.frameAnimationSpeed, LEFT, True)
                self.animationState = ANIMATION_HEALTHLESS_POWERLESS
        elif self.currentHealth < self.maxHealth/3:
            if self.animationState is not ANIMATION_HEALTHLESS:
                self.animationIdle = Animation(self.imageIdleHealthless, self.frameAnimationSpeed, LEFT, True)
                self.animationWalk = Animation(self.imageWalkHealthless, self.frameAnimationSpeed, LEFT, True)
                self.animationState = ANIMATION_HEALTHLESS
        elif self.currentEnergy < self.maxEnergy / 3:
            if self.animationState is not ANIMATION_POWERLESS:
                self.animationIdle = Animation(self.imageIdlePowerless, self.frameAnimationSpeed, LEFT, True)
                self.animationWalk = Animation(self.imageWalkPowerless, self.frameAnimationSpeed, LEFT, True)
                self.animationState = ANIMATION_POWERLESS
        else:
            if self.animationState is not ANIMATION_NORMAL:
                self.animationIdle = Animation(self.imageIdle, self.frameAnimationSpeed, LEFT, True)
                self.animationWalk = Animation(self.imageWalk, self.frameAnimationSpeed, LEFT, True)
                self.animationState = ANIMATION_NORMAL

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
        self.mapData.playerIsDead()
        self.isAlive = False
        self.target.kill()
        self.kill()

    def onSpike(self):
        self.kill()

    def notify(self, event):
        self.nextState = self.state.handleInput(self, event)

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
        self.rechargeCooldown.update()

        # For invincibitlity
        self.invincibleCooldown.update()

    def shootBullet(self):
        if self.gunCooldown.isZero and self.currentEnergy>0:
            self.soundShootGun.play()

            bullet = PlayerBullet(self.target.rect.centerx, self.target.rect.centery, self.target.powerx*PLAYER_BULLET_SPEED, self.target.powery*PLAYER_BULLET_SPEED,self.mapData)
            self.mapData.camera.add(bullet)
            self.mapData.allSprites.add(bullet)
            self.mapData.friendlyBullets.add(bullet)
            self.gunCooldown.start()
            self.currentEnergy -= 1

    def hurt(self, damage):
        if self.invincibleCooldown.isZero:

            self.currentHealth -= damage
            self.hurtSound.play()
            if self.currentHealth<0:
                self.currentHealth = 0

            self.checkIfIsAlive()
            self.invincibleOnHit()

    def checkIfIsAlive(self):
        if self.currentHealth <= 0:
            self.dead()

    def invincibleOnHit(self):
        self.invincibleCooldown.start()

    def charge(self):
        if self.rechargeCooldown.isZero and self.currentEnergy < self.maxEnergy:
            self.currentEnergy += 1
            self.rechargeCooldown.start()
