__author__ = 'Bobsleigh'

from ldLib.collision.collisionTile import collisionWithTile
from app.settings import *
from ldLib.collision.CollisionRules.CollisionRule import CollisionRule

class CollisionWithEnergyCharge(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        if collisionWithTile(sprite, ENERGY_CHARGE, sprite.mapData):
            sprite.charge()
        else:
            sprite.notOnCharge()

    def onMoveY(self, sprite):
        if collisionWithTile(sprite, ENERGY_CHARGE, sprite.mapData):
            sprite.charge()
        else:
            sprite.notOnCharge()