__author__ = 'Bobsleigh'

from ldLib.collision.collisionTile import collisionWithTile
from app.settings import *
from ldLib.collision.CollisionRules.CollisionRule import CollisionRule

class CollisionWithSolidDetonate(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        if collisionWithTile(sprite, SOLID, sprite.mapData):
            sprite.detonate()

    def onMoveY(self, sprite):
        if collisionWithTile(sprite, SOLID, sprite.mapData):
            sprite.detonate()