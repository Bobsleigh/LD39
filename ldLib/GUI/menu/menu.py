import pygame

from ldLib.GUI.menu.option import Option
from ldLib.GUI.menu.selector import Selector
from app.settings import *


class Menu(pygame.sprite.Sprite):
    def __init__(self,dimension,fontSize=30,spaceHeightFactor=0.7):
        super().__init__()

        # Menu center
        self.x = dimension.left
        self.y = dimension.top

        # Menu dimension
        self.menuWidth = dimension.width
        self.menuHeight = dimension.height
        self.menuFontSize = fontSize
        self.spaceHeightFactor = spaceHeightFactor

        # Menu list
        self.optionList = []

        #All sprite
        self.spritesMenu = pygame.sprite.Group()
        self.image = pygame.Surface((self.menuWidth, self.menuHeight))
        self.rect = dimension

        self.selected = True

    def addOption(self,name,method):
        self.optionList.append(Option(name,method,self.menuFontSize))
        self.createMenu()

    def createMenu(self):

        # Default select opt. 1
        self.optionList[0].isSelected = True

        # Mecanics.
        self.optNum = len(self.optionList)
        self.setOptionSize()
        self.selector = Selector(self.optNum)

        # Add to sprite
        for option in self.optionList:
            self.spritesMenu.add(option)

        #Draw the menu
        self.image.fill(WHITE)
        self.spritesMenu.draw(self.image)

    def setOptionSize(self):
        # Button real space
        spaceWidth = self.menuWidth
        spaceHeight = self.menuHeight / (self.optNum)

        for option in self.optionList:
            option.image = pygame.Surface([spaceWidth*0.9,spaceHeight*self.spaceHeightFactor])
            option.rect = option.image.get_rect()

            count = self.optionList.index(option)
            option.rect.x = 0
            option.rect.y = count*spaceHeight

            option.button = option.rect.inflate(-option.image.get_height()*0.2,-option.image.get_height()*0.2)
            option.button.x = option.image.get_height()*0.1
            option.button.y = option.image.get_height()*0.1

            option.textPos =[(option.image.get_width()-option.printedName.get_width())*0.5,(option.image.get_height()-option.printedName.get_height())*0.5]

    def notify(self, event):
        if self.selected:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveUp()
                    self.optionList[self.selector.vPos].select()
                elif event.key == pygame.K_DOWN:
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveDown()
                    self.optionList[self.selector.vPos].select()
                elif event.key == pygame.K_SPACE:
                    self.optionList[self.selector.vPos].doOption()
                elif event.key == pygame.K_RETURN:
                    self.optionList[self.selector.vPos].doOption()

    def update(self):
        for opt in self.optionList:
            opt.update()

        for option in self.spritesMenu.sprites():
            self.image.blit(option.image, option.rect)

        #self.spritesMenu.draw(self.image)

        if not self.selected:
            self.optionList[self.selector.vPos].deselect()
        else:
            self.optionList[self.selector.vPos].select()

    def draw(self, target):
        target.blit(self.image, self.rect)