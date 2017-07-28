__author__ = 'Bobsleigh'

from ldLib.collision.collisionTile import collisionWithTile
from app.settings import *
from ldLib.Sprites.Player.IdleState import IdleState
from ldLib.collision.CollisionRules.CollisionRule import CollisionRule

class CollisionWithSolid(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        if collisionWithTile(sprite, SOLID, sprite.mapData):
            if sprite.speedx > 0:
                sprite.x = ((sprite.x + sprite.collisionMask.rect.width) // sprite.mapData.tmxData.tilewidth) * sprite.mapData.tmxData.tilewidth - sprite.collisionMask.rect.width
            else:
                sprite.x = (sprite.x // sprite.mapData.tmxData.tilewidth + 1) * sprite.mapData.tmxData.tilewidth
            sprite.collisionMask.rect.x = sprite.x

    def onMoveY(self, sprite):
        if collisionWithTile(sprite, SOLID, sprite.mapData):
            if sprite.speedy > 0:
                sprite.y = ((sprite.y + sprite.collisionMask.rect.height) // sprite.mapData.tmxData.tileheight) * sprite.mapData.tmxData.tileheight - sprite.collisionMask.rect.height
                if not isinstance(sprite.state, IdleState):
                    sprite.state = IdleState()
            else:
                sprite.y = (sprite.y // sprite.mapData.tmxData.tileheight + 1) * sprite.mapData.tmxData.tileheight
            sprite.collisionMask.rect.y = sprite.y