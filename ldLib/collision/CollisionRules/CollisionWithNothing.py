__author__ = 'Bobsleigh'

from ldLib.collision.collisionTile import collisionExclusivelyWithTile
from app.settings import *
from ldLib.Sprites.Player.IdleState import IdleState
from ldLib.Sprites.Player.JumpState import JumpState
from ldLib.collision.CollisionRules.CollisionRule import CollisionRule

class CollisionWithNothing(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        pass

    def onMoveY(self, sprite):
        pass