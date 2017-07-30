from app.settings import *

from ldLib.GUI.EnergyBar import EnergyBar
from ldLib.GUI.LifeBar import LifeBar

class LevelHUD:
    def __init__(self,scenedata,player,boss=None):
        playerLifeBar = LifeBar(player, PLAYER_LIFE_X, PLAYER_LIFE_Y, PLAYER_LIFE_WIDTH, PLAYER_LIFE_HEIGHT)
        scenedata.spritesHUD.add(playerLifeBar)
        energyBar = EnergyBar(player, PLAYER_ENERGY_X, PLAYER_ENERGY_Y, PLAYER_ENERGY_WIDTH, PLAYER_ENERGY_HEIGHT)
        scenedata.spritesHUD.add(energyBar)
        if boss is not None:
            #Add boss' life bar here.
            pass

