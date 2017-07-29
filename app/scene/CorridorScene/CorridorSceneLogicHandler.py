from ldLib.scene.LogicHandler import LogicHandler
from app.scene.TopDownPhysics import TopDownPhysics
from ldLib.collision.collisionNotifySprite import collisionNotifySprite
from app.settings import *

class CorridorSceneLogicHandler(LogicHandler):
    def __init__(self, gameData):
        super().__init__(gameData)
        self.physics = TopDownPhysics(gameData.sceneData)

    def handle(self):
        super().handle()
        self.physics.update()
        self.handleZoneCollision()

    def handleZoneCollision(self):
        player = self.sceneData.player
        for obj in self.sceneData.tmxData.objects:
            if self.isPlayerIsInZone(player, obj) == True:
                if obj.name == "OutZone":
                    self.sceneData.nextScene = self.sceneData.nextLevel

    def isPlayerIsInZone(self, player, zone):
        if player.rect.centerx >= zone.x and \
                        player.rect.centerx <= zone.x + zone.width and \
                        player.rect.centery >= zone.y and \
                        player.rect.centery <= zone.y + zone.height:
            return True
        else:
            return False