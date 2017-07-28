__author__ = 'Bobsleigh'

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
NONE = 4

COLLISION_LAYER = 0

def collisionTile(sprite, tileType, mapData):
    tile = None
    direction = None

    tile, direction = rightCollision(sprite, tileType, mapData)
    tile, direction = leftCollision(sprite, tileType, mapData)
    tile, direction = downCollision(sprite, tileType, mapData)
    tile, direction = upCollision(sprite, tileType, mapData)

    if tile != NONE:
        return True
    else:
        return False

def rightCollision(sprite, tileType, map):
    tileWidth = map.tmxData.tilewidth
    tileHeight = map.tmxData.tileheight

    if sprite.collisionMask.rect.right > 0: #To prevent get_tile_gid from crashing
        upRightTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.right)/tileWidth, (sprite.collisionMask.rect.top + 1)/tileHeight, COLLISION_LAYER)
        downRightTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.right)/tileWidth, (sprite.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER)

        if (upRightTileGid  == tileType or downRightTileGid == tileType):
            print("RIGHT")
            return tileType, RIGHT
        else:
            return NONE, RIGHT

def leftCollision(sprite, tileType, map):
    tileWidth = map.tmxData.tilewidth
    tileHeight = map.tmxData.tileheight

    upLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left)/tileWidth, (sprite.collisionMask.rect.top+1)/tileHeight, COLLISION_LAYER)
    downLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left)/tileWidth, (sprite.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER)

    if (upLeftTileGid  == tileType or downLeftTileGid  == tileType):
        print("LEFT")
        return tileType, LEFT
    else:
        return NONE, LEFT

def downCollision(sprite, tileType, map):
    tileWidth = map.tmxData.tilewidth
    tileHeight = map.tmxData.tileheight

    downLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left+1)/tileWidth, (sprite.collisionMask.rect.bottom)/tileHeight, COLLISION_LAYER)
    downRightTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.right - 1)/tileWidth, (sprite.collisionMask.rect.bottom)/tileHeight, COLLISION_LAYER)
    #downMidTileGID = map.tmxData.get_tile_gid((sprite.collisionMask.rect.centerx)/tileWidth, (sprite.collisionMask.rect.bottom)/tileHeight, COLLISION_LAYER)

    if downLeftTileGid == tileType or downRightTileGid == tileType:# or downMidTileGID == tileType:
        print("DOWN")
        return tileType, DOWN
    else:
        return NONE, DOWN


def upCollision(sprite, tileType, map):
    tileWidth = map.tmxData.tilewidth
    tileHeight = map.tmxData.tileheight

    upLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left+1)/tileWidth, (sprite.collisionMask.rect.top)/tileHeight, COLLISION_LAYER)
    upRightTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.right - 1)/tileWidth, (sprite.collisionMask.rect.top)/tileHeight, COLLISION_LAYER)
    #upMidTileGid = map.tmxData.get_tile_gid(sprite.collisionMask.rect.centerx/tileWidth, (sprite.collisionMask.rect.top)/tileHeight, COLLISION_LAYER)

    if upLeftTileGid == tileType or upRightTileGid == tileType:# or upMidTileGid == tileType:
        print("UP")
        return tileType, UP
    else:
        return NONE, UP

def collisionWithTile(sprite, tileType, map):
    tileWidth = map.tmxData.tilewidth
    tileHeight = map.tmxData.tileheight

    upLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left)/tileWidth, (sprite.collisionMask.rect.top)/tileHeight, COLLISION_LAYER)
    upRightTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.right - 1)/tileWidth, (sprite.collisionMask.rect.top)/tileHeight, COLLISION_LAYER)
    downLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left)/tileWidth, (sprite.collisionMask.rect.bottom - 1)/tileHeight, COLLISION_LAYER)
    downRightTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.right - 1)/tileWidth, (sprite.collisionMask.rect.bottom - 1)/tileHeight, COLLISION_LAYER)

    if upLeftTileGid == tileType or upRightTileGid == tileType or downLeftTileGid == tileType or downRightTileGid == tileType:
        return True
    else:
        return False

def collisionExclusivelyWithTile(sprite, tileType, map):
    tileWidth = map.tmxData.tilewidth
    tileHeight = map.tmxData.tileheight

    upLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left)/tileWidth, (sprite.collisionMask.rect.top)/tileHeight, COLLISION_LAYER)
    upRightTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.right - 1)/tileWidth, (sprite.collisionMask.rect.top)/tileHeight, COLLISION_LAYER)
    downLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left)/tileWidth, (sprite.collisionMask.rect.bottom - 1)/tileHeight, COLLISION_LAYER)
    downRightTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.right - 1)/tileWidth, (sprite.collisionMask.rect.bottom - 1)/tileHeight, COLLISION_LAYER)

    if upLeftTileGid == tileType and upRightTileGid == tileType and downLeftTileGid == tileType and downRightTileGid == tileType:
        return True
    else:
        return False