from ldLib.scene.LogicHandler import LogicHandler
from app.scene.TopDownPhysics import TopDownPhysics
from ldLib.collision.collisionNotifySprite import collisionNotifySprite
from app.settings import *


class CorridorSceneLogicHandler(LogicHandler):
    def __init__(self, gameData):
        super().__init__(gameData)
        self.physics = TopDownPhysics(gameData.sceneData)

        # Set infinite energy
        self.sceneData.player.energyConsume = 0

    def handle(self):
        super().handle()
        self.physics.update()
        self.handleZoneCollision()
        self.updateMessageBox()

    def handleZoneCollision(self):
        player = self.sceneData.player
        for item in self.sceneData.messageBoxes:
            item[1] = False

        for obj in self.sceneData.tmxData.objects:
            if self.isPlayerIsInZone(player, obj) == True:
                if obj.name == "OutZone":
                    self.sceneData.nextScene = self.sceneData.nextLevel
                elif obj.name == "MessageZone":
                    self.sceneData.messageBoxes[int(obj.index)][1] = True
                elif TAG_MARIE == 1:
                    if obj.name == "HurtZone":
                        self.sceneData.turret1.needToOpen=True

    def isPlayerIsInZone(self, player, zone):
        if player.rect.centerx >= zone.x and \
                        player.rect.centerx <= zone.x + zone.width and \
                        player.rect.centery >= zone.y and \
                        player.rect.centery <= zone.y + zone.height:
            return True
        else:
            return False

    def updateMessageBox(self):
        for item in self.sceneData.messageBoxes:
            sprite = item[0]
            if item[1]== True:
                self.sceneData.spritesHUD.add(sprite)
            else:
                if self.sceneData.spritesHUD.has(sprite):
                    self.sceneData.spritesHUD.remove(sprite)


