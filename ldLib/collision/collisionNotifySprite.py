__author__ = 'Bobsleigh'

from ldLib.collision.collisionTile import *

def collisionNotifySprite(sprite, tileType, mapData):
    tile, direction = rightCollision(sprite, tileType, mapData)
    if tile != NONE:
        sprite.onCollision(tile, direction)
    tile, direction = leftCollision(sprite, tileType, mapData)
    if tile != NONE:
        sprite.onCollision(tile, direction)
    tile, direction = downCollision(sprite, tileType, mapData)
    if tile != NONE:
        sprite.onCollision(tile, direction)
    tile, direction = upCollision(sprite, tileType, mapData)
    if tile != NONE:
        sprite.onCollision(tile, direction)

# def collisionNotifySprite(sprite, tileType, mapData):
#     collisions = []
#
#     tile, direction = rightCollision(sprite, tileType, mapData)
#     if tile != NONE:
#         collisions.append((tile, direction))
#
#     tile, direction = leftCollision(sprite, tileType, mapData)
#     if tile != NONE:
#         collisions.append((tile, direction))
#
#     tile, direction = downCollision(sprite, tileType, mapData)
#     if tile != NONE:
#         collisions.append((tile, direction))
#
#     tile, direction = upCollision(sprite, tileType, mapData)
#     if tile != NONE:
#         collisions.append((tile, direction))
#
#     if collisions:
#         sprite.notifyCollisions(collisions)