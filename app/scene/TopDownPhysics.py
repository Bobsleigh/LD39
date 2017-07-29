from app.settings import *

class TopDownPhysics:
    def __init__(self, sceneData):
        self.sceneData = sceneData

    def update(self):
        self.applyFriction(self.sceneData.allSprites)
        self.applyGravity(self.sceneData.allSprites)

    def applyFriction(self, allSprites):
        for sprite in allSprites:
            try:
                if sprite.isFrictionApplied:
                    pass
                    if sprite.speedx > 0 and sprite.speedx - FRICTION > 0:
                        sprite.speedx -= FRICTION
                    elif sprite.speedx > 0:
                        sprite.speedx = 0

                    if sprite.speedx < 0 and sprite.speedx + FRICTION < 0:
                        sprite.speedx += FRICTION
                    elif sprite.speedx < 0:
                        sprite.speedx = 0

                    if sprite.speedy > 0 and sprite.speedy - FRICTION > 0:
                        sprite.speedy -= FRICTION
                    elif sprite.speedy > 0:
                        sprite.speedy = 0

                    if sprite.speedy < 0 and sprite.speedy + FRICTION < 0:
                        sprite.speedy += FRICTION
                    elif sprite.speedy < 0:
                        sprite.speedy = 0
            except AttributeError:
                pass

    def applyGravity(self, allSprites):
        for sprite in allSprites:
            try:
                if sprite.isGravityApplied:
                    sprite.speedy += GRAVITY
            except AttributeError:
                pass

