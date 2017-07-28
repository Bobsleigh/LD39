__author__ = 'Bobsleigh'

from ldLib.collision.collisionTile import collisionWithTile
from app.settings import *
from ldLib.Sprites.Player.IdleState import IdleState
from ldLib.Sprites.Player.ClimbingState import ClimbingState
from ldLib.collision.CollisionRules.CollisionRule import CollisionRule

class CollisionWithLadder(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        if collisionWithTile(sprite, LADDER, sprite.mapData):
            if not isinstance(sprite.state, ClimbingState):
                sprite.state = ClimbingState()

    def onMoveY(self, sprite):
        pass