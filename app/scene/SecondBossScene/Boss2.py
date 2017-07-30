import pygame, os

from app.scene.SecondBossScene.Boss2AI import Boss2AI
from app.settings import *
from ldLib.collision.collisionMask import CollisionMask
from ldLib.tools.ImageBox import ImageBox
from ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from ldLib.Sprites.Player.IdleState import IdleState
from ldLib.tools.Cooldown import Cooldown


class Boss2(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData, max_health=10):
        super().__init__()

        self.name = "Boss2"

        self.imageBase = pygame.image.load(os.path.join('img', 'laser-boss.png'))
        self.imageBase.set_colorkey(COLORKEY)

        self.imageShapeLeft = None
        self.imageShapeRight = None

        self.imageTransparent = pygame.Surface((1, 1),pygame.SRCALPHA)

        self.setShapeImage()
        self.image = self.imageShapeRight

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
        # Life bar
        self.maxHealth = 200
        self.currentHealth = 200

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

        self.mapData = sceneData

        self.isAlive = True

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.collisionRules = []
        self.collisionRules.append(CollisionWithSolid())

        self._state = IdleState()
        self.AI = Boss2AI(self, self.mapData)

        self.invincibleCooldown = Cooldown(60)
        self.flashduration = 8

        self.hurtSound = pygame.mixer.Sound(os.path.join('music', 'Hit_Hurt.wav'))
        self.hurtSound.set_volume(.25)

        self.touchDamage = 10

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

        if self.speedx > 0:
            self.image = self.imageShapeRight
            self.facingSide = RIGHT
        if self.speedx < 0:
            self.image = self.imageShapeLeft
            self.facingSide = LEFT

        # Replace make visual flash in invincible mode.
        # if not self.invincibleCooldown.isZero:
        #     if self.flashduration-3 <= self.invincibleCooldown.value % self.flashduration:
        #         self.image = self.imageTransparent

        self.updateCollisionMask()
        self.updatePressedKeys()
        self.updateCooldowns()

    def updateCooldowns(self):
        # For invincibitlity
        self.invincibleCooldown.update()

    def shootLaser(self):
        self.mapData.camera.add()

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
        if self.speedy > 0 and self.speedy > self.maxSpeedy:
            self.speedy = self.maxSpeedy
        if self.speedy < 0 and self.speedy < -self.maxSpeedy:
            self.speedy = -self.maxSpeedy

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

    def dead(self):
        self.isAlive = False
        for laser in self.mapData.laserGroup:
            laser.kill()
        self.kill()

    def onSpike(self):
        self.kill()

    def hurt(self, damage):
        if self.invincibleCooldown.isZero:
            self.currentHealth -= damage
            self.AI.wasHurt = True
            self.hurtSound.play()

            self.checkIfIsAlive()
            self.invincibleOnHit()

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

    def invincibleOnHit(self):
        self.invincibleCooldown.start()

    def checkIfIsAlive(self):
        if self.currentHealth <= 0:
            self.dead()