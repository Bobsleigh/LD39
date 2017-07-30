import pygame, os, random

from app.settings import *
from ldLib.collision.collisionMask import CollisionMask
from ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from ldLib.Sprites.SecondBoss.IdleState import IdleState
from ldLib.Sprites.SecondBoss.ShootingAllLasersState import ShootingAllLasersState
from ldLib.tools.Cooldown import Cooldown


class LaserTurret(pygame.sprite.Sprite):
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

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.collisionRules = []
        self.collisionRules.append(CollisionWithSolid())

        self.hurtSound = pygame.mixer.Sound(os.path.join('music', 'Hit_Hurt.wav'))
        self.hurtSound.set_volume(.25)

        self.shootingSpeed = 400 + random.randint(0, 50)
        self.shootingCooldown = Cooldown(self.shootingSpeed)
        self.shootingCooldown.start()

        self._state = IdleState()
        self.state = IdleState()

        self.touchDamage = 10

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state.exit(self)
        self._state = value
        self._state.enter(self)


    def setShapeImage(self):
        self.imageShapeLeft = pygame.transform.flip(self.imageBase, True, False)
        self.imageShapeRight = self.imageBase

    def update(self):
        self.updateCooldowns()

    def updateCooldowns(self):
        if self.shootingCooldown.isZero:
            self.state = ShootingAllLasersState(self, self.sceneData)
            self.shootingCooldown.start()
        if self.shootingCooldown.value == self.shootingSpeed - 60:
            self.state = IdleState()

        self.shootingCooldown.update()
        self.state.update(self, self.sceneData)

    def shootLaser(self):
        self.mapData.camera.add()

    def dead(self):
        self.isAlive = False
        for laser in self.mapData.laserGroup:
            laser.kill()
        self.kill()