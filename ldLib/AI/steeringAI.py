import math
from app.settings import *

class SteeringAI:
    def __init__(self, mapData, userRect, userMaxSpeedx, userMaxSpeedy):
        self.mapData = mapData
        self.rect = userRect
        self.userSpeedx = userMaxSpeedx
        self.userSpeedy = userMaxSpeedy

    def getAction(self):
        norm = self.vectorNorm(self.mapData.player.rect.x - self.rect.x, self.mapData.player.rect.y - self.rect.y)
        desiredSpdX = float(self.mapData.player.rect.x - self.rect.x)/norm * self.userSpeedx
        desiredSpdY = float(self.mapData.player.rect.y - self.rect.y)/norm * self.userSpeedy

        steeringX = desiredSpdX
        steeringY = desiredSpdY

        return steeringX, steeringY


    def vectorNorm(self,x,y):
        result = math.sqrt(x**2+y**2)
        if result == 0:
            return 1

        return result