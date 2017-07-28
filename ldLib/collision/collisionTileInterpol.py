__author__ = 'Bobsleigh'


def collisionTileInterpol(sprite, tileType, mapData):
    if rightCollision(sprite, tileType, mapData) or leftCollision(sprite, tileType, mapData) or downCollision(sprite, tileType, mapData) or upCollision(sprite, tileType, mapData):
        pass


def rightCollision(self,sprite, map):

    # mapHeight = map.tmxData.height * tileHeight
    i=0

    if sprite.collisionMask.rect.right + sprite.speedx > 0:
        if sprite.speedx >= self.tileWidth: #Si on va plus vite qu'une tile/seconde
            while sprite.collisionMask.rect.right+i*self.tileWidth < sprite.collisionMask.rect.right + sprite.speedx:
                if sprite.collisionMask.rect.right+i*self.tileWidth >= self.mapWidth:
                    j=0
                    while map.tmxData.get_tile_gid((self.mapWidth - 1 - j*self.tileWidth)/self.tileWidth, sprite.collisionMask.rect.top/self.tileHeight, COLLISION_LAYER) == self.mapData.solidGID and map.tmxData.get_tile_gid((self.mapWidth - 1- j*self.tileWidth)/self.tileWidth, (sprite.collisionMask.rect.bottom)/self.tileHeight, COLLISION_LAYER) == self.mapData.solidGID:
                        j += 1
                    sprite.onCollision(self.mapData.solidGID, RIGHT)
                    return

                upRightTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.right + i*self.tileWidth)/self.tileWidth, sprite.collisionMask.rect.top/self.tileHeight, COLLISION_LAYER)
                downRightTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.right + i*self.tileWidth)/self.tileWidth, (sprite.collisionMask.rect.bottom-1)/self.tileHeight, COLLISION_LAYER)

                if (upRightTileGid  == self.mapData.solidGID or downRightTileGid  == self.mapData.solidGID) and sprite.speedx > 0 and sprite.facingSide == RIGHT:
                    while map.tmxData.get_tile_gid((sprite.collisionMask.rect.right + 1)/self.tileWidth, sprite.collisionMask.rect.top/self.tileHeight, COLLISION_LAYER) != self.mapData.solidGID and map.tmxData.get_tile_gid((sprite.collisionMask.rect.right + 1)/self.tileWidth, (sprite.collisionMask.rect.bottom-1)/self.tileHeight, COLLISION_LAYER) != self.mapData.solidGID:
                        sprite.collisionMask.rect.right += 1
                        sprite.onCollision(self.mapData.solidGID, RIGHT)
                i += 1

        else:
            upRightTileGid = self.map.tmxData.get_tile_gid((sprite.collisionMask.rect.right + sprite.speedx)/self.tileWidth, (sprite.collisionMask.rect.top + 1)/self.tileHeight, COLLISION_LAYER)
            downRightTileGid = self.map.tmxData.get_tile_gid((sprite.collisionMask.rect.right + sprite.speedx)/self.tileWidth, (sprite.collisionMask.rect.bottom-1)/self.tileHeight, COLLISION_LAYER)

            if (upRightTileGid  == self.mapData.solidGID or downRightTileGid == self.mapData.solidGID) and sprite.speedx > 0:
                sprite.onCollision(self.mapData.solidGID, RIGHT)
            elif upRightTileGid  == ENTRANCEWALL or downRightTileGid == ENTRANCEWALL:
                sprite.onCollision(ENTRANCEWALL, RIGHT)
            elif upRightTileGid  == SPRING or downRightTileGid == SPRING:
                sprite.onCollision(SPRING, RIGHT)

def leftCollision(self,sprite, map):
    tileWidth = map.tmxData.tilewidth
    tileHeight = map.tmxData.tileheight
    # mapWidth = map.tmxData.width * tileWidth
    # mapHeight = map.tmxData.height * tileHeight
    i = 0

    if -sprite.speedx >= tileWidth:
        while sprite.collisionMask.rect.x-i*tileWidth > sprite.collisionMask.rect.x + sprite.speedx:
            if sprite.collisionMask.rect.x-i*tileWidth <= 0:
                j=0
                while map.tmxData.get_tile_gid((0 + j*tileWidth)/tileWidth, sprite.collisionMask.rect.top/tileHeight, COLLISION_LAYER) == self.mapData.solidGID and map.tmxData.get_tile_gid((0 + j*tileWidth)/tileWidth, (sprite.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER) == self.mapData.solidGID:
                    j += 1
                    sprite.onCollision(self.mapData.solidGID, LEFT)
                return

            upLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left - i*tileWidth)/tileWidth, sprite.collisionMask.rect.top/tileHeight, COLLISION_LAYER)
            downLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left - i*tileWidth)/tileWidth, (sprite.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER)

            if (upLeftTileGid  == self.mapData.solidGID or downLeftTileGid  == self.mapData.solidGID) and sprite.facingSide == LEFT:
                while map.tmxData.get_tile_gid((sprite.collisionMask.rect.left)/tileWidth, sprite.collisionMask.rect.top/tileHeight, COLLISION_LAYER) != self.mapData.solidGID and map.tmxData.get_tile_gid((sprite.collisionMask.rect.left)/tileWidth, (sprite.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER) != self.mapData.solidGID:
                    sprite.collisionMask.rect.left -= 1
                sprite.onCollision(self.mapData.solidGID, LEFT)
            i += 1

    else:
        upLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left + sprite.speedx)/tileWidth, sprite.collisionMask.rect.top/tileHeight, COLLISION_LAYER)
        downLeftTileGid = map.tmxData.get_tile_gid((sprite.collisionMask.rect.left + sprite.speedx)/tileWidth, (sprite.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER)


        if (upLeftTileGid  == self.mapData.solidGID or downLeftTileGid  == self.mapData.solidGID) and sprite.speedx < 0:
            #while map.tmxData.get_tile_gid((player.collisionMask.rect.left)/tileWidth, player.collisionMask.rect.top/tileHeight, COLLISION_LAYER) != self.mapData.solidGID and map.tmxData.get_tile_gid((player.collisionMask.rect.left)/tileWidth, (player.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER) != self.mapData.solidGID:
                 #player.collisionMask.rect.left -= 1
            sprite.onCollision(self.mapData.solidGID, LEFT)
        elif upLeftTileGid  == ENTRANCEWALL or downLeftTileGid  == ENTRANCEWALL:
            sprite.onCollision(ENTRANCEWALL, LEFT)
        elif (upLeftTileGid  == SPRING or downLeftTileGid  == SPRING) and sprite.speedx < 0:
            sprite.onCollision(SPRING, LEFT)


def downCollision(self,sprite, map):
    tileWidth = map.tmxData.tilewidth
    tileHeight = map.tmxData.tileheight
    # mapWidth = map.tmxData.width * tileWidth
    # mapHeight = map.tmxData.height * tileHeight

    downLeftTileGid = map.tmxData.get_tile_gid((sprite.rect.left+1)/tileWidth, (sprite.rect.bottom + sprite.speedy)/tileHeight, COLLISION_LAYER)
    downRightTileGid = map.tmxData.get_tile_gid((sprite.rect.right-1)/tileWidth, (sprite.rect.bottom + sprite.speedy)/tileHeight, COLLISION_LAYER)
    downMidTileGID = map.tmxData.get_tile_gid((sprite.rect.centerx)/tileWidth, (sprite.rect.bottom + sprite.speedy)/tileHeight, COLLISION_LAYER)

    if downLeftTileGid == self.mapData.solidGID or downRightTileGid == self.mapData.solidGID or downMidTileGID == self.mapData.solidGID:
        sprite.onCollision(self.mapData.solidGID, DOWN)
    elif downLeftTileGid == ENTRANCEWALL or downRightTileGid == ENTRANCEWALL  or downMidTileGID == ENTRANCEWALL:
        sprite.onCollision(ENTRANCEWALL, DOWN)
    elif downLeftTileGid == SPRING or downRightTileGid == SPRING  or downMidTileGID == SPRING:
        sprite.onCollision(SPRING, DOWN)
    else:
        sprite.onCollision(NONE, DOWN)


def upCollision(self,sprite, map):
    tileWidth = map.tmxData.tilewidth
    tileHeight = map.tmxData.tileheight

    upLeftTileGid = map.tmxData.get_tile_gid((sprite.rect.left+1)/tileWidth, (sprite.rect.top + sprite.speedy)/tileHeight, COLLISION_LAYER)
    upRightTileGid = map.tmxData.get_tile_gid((sprite.rect.right - 1)/tileWidth, (sprite.rect.top + sprite.speedy)/tileHeight, COLLISION_LAYER)
    upMidTileGid = map.tmxData.get_tile_gid(sprite.rect.centerx/tileWidth, (sprite.rect.top + sprite.speedy)/tileHeight, COLLISION_LAYER)

    if upLeftTileGid == self.mapData.solidGID or upRightTileGid == self.mapData.solidGID or upMidTileGid == self.mapData.solidGID:
        sprite.onCollision(self.mapData.solidGID, UP)

    elif upLeftTileGid == ENTRANCEWALL or upRightTileGid == ENTRANCEWALL:
        sprite.onCollision(ENTRANCEWALL, UP)
    elif upLeftTileGid == LADDER or upRightTileGid == LADDER or upMidTileGid == LADDER:
        sprite.onCollision(LADDER, UP)
    else:
        sprite.onCollision(NONE, UP)