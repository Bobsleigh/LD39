from app.settings import *

from ldLib.GUI.EnergyBar import EnergyBar
from ldLib.GUI.LifeBar import LifeBar
from ldLib.GUI.TextSprite import TextSprite


class LevelHUD:
    def __init__(self,scenedata,player,boss=None):
        playerLifeBar = LifeBar(player, PLAYER_LIFE_X, PLAYER_LIFE_Y, PLAYER_LIFE_WIDTH, PLAYER_LIFE_HEIGHT)
        scenedata.spritesHUD.add(playerLifeBar)
        lifeLabel = TextSprite("Life", PLAYER_LIFE_X + 8, PLAYER_LIFE_Y + PLAYER_LIFE_HEIGHT)
        scenedata.spritesHUD.add(lifeLabel)

        energyBar = EnergyBar(player, PLAYER_ENERGY_X, PLAYER_ENERGY_Y, PLAYER_ENERGY_WIDTH, PLAYER_ENERGY_HEIGHT)
        scenedata.spritesHUD.add(energyBar)
        energyLabel = TextSprite("Energy", PLAYER_ENERGY_X + PLAYER_ENERGY_WIDTH-120, PLAYER_ENERGY_Y + PLAYER_ENERGY_HEIGHT)
        scenedata.spritesHUD.add(energyLabel)

        if boss is not None:
            #Add boss' life bar here
            bossName = TextSprite(boss.name,BOSS_LIFE_X+8,BOSS_LIFE_Y-DIALOG_TEXT_SIZE-5)
            scenedata.spritesHUD.add(bossName)

            bossLifeBar = LifeBar(boss, BOSS_LIFE_X, BOSS_LIFE_Y, BOSS_LIFE_WIDTH, BOSS_LIFE_HEIGHT)
            scenedata.spritesHUD.add(bossLifeBar)

