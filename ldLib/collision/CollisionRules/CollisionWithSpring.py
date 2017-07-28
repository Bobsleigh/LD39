__author__ = 'Bobsleigh'

from ldLib.collision.collisionTile import collisionWithTile
from ldLib.collision.CollisionRules.CollisionRule import CollisionRule
from ldLib.Sprites.Player.JumpState import JumpState
from app.settings import *

class CollisionWithSpring(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        if ((sprite.collisionMask.rect.bottom - 1) % sprite.mapData.tmxData.tileheight) > sprite.mapData.tmxData.tileheight/2: # Check if the bottom of the sprite collides with the lower half of the spring
            if collisionWithTile(sprite, SPRING, sprite.mapData):
                if sprite.speedx > 0:
                    sprite.x = ((sprite.x + sprite.collisionMask.rect.width) // sprite.mapData.tmxData.tilewidth) * sprite.mapData.tmxData.tilewidth - sprite.collisionMask.rect.width
                else:
                    sprite.x = (sprite.x // sprite.mapData.tmxData.tilewidth + 1) * sprite.mapData.tmxData.tilewidth
                sprite.collisionMask.rect.x = sprite.x

    def onMoveY(self, sprite):
        if ((sprite.collisionMask.rect.bottom - 1) % sprite.mapData.tmxData.tileheight) <= sprite.mapData.tmxData.tileheight/2: # Check if the bottom of the sprite collides with the higher half of the spring
            if collisionWithTile(sprite, SPRING, sprite.mapData):
                if sprite.speedy > 0:
                    sprite.speedy = -sprite.springJumpSpeed
                    sprite.state = JumpState()