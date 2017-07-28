__author__ = 'Bobsleigh'

import pygame

from app.settings import *
from ldLib.GUI.ObjectMenu.ObjectOption import ObjectOption
from ldLib.GUI.ObjectMenu.ObjectSelector import ObjectSelector


#For a very short message only

class ObjectMenu(pygame.sprite.Sprite):
    def __init__(self, dimensionRect, objectList, spaceHeightFactor=1, fontSize=20):
        super().__init__()

        # Menu center
        self.x = dimensionRect.left
        self.y = dimensionRect.top

        # Menu dimension
        self.menuWidth = dimensionRect.width
        self.menuHeight = dimensionRect.height
        self.menuFontSize = fontSize
        self.spaceHeightFactor = spaceHeightFactor
        self.cursorToTextSpacing = 5

        # Generate Option List
        self.optionList = []

        for string in objectList:
            self.optionList.append(ObjectOption(string, self.menuFontSize))

        #All sprite
        self.spritesOptions = pygame.sprite.Group()
        self.image = pygame.Surface((self.menuWidth, self.menuHeight))
        self.rect = dimensionRect

        self._isActivated = False

        # Default select opt. 1
        self.optionList[0].isSelected = True

        # Selector
        self.numberOfOptions = len(self.optionList)
        self.selector = ObjectSelector(self.numberOfOptions)
        self.setOptionSize()

        # Add to sprite
        for option in self.optionList:
            self.spritesOptions.add(option)

        self.chosenOptionIndex = None

        #Scrolling parameters
        self.displayedOptions = self.menuHeight // self.optionList[0].printedName.get_height()
        self.scrolledPosition = 0

    def setOptionSize(self):
        # Button real space
        spaceWidth = self.menuWidth
        spaceHeight = self.menuHeight / (self.numberOfOptions)
        optionHeight = self.optionList[0].printedName.get_height()
        numberOfOptionsDisplayed = spaceHeight//optionHeight

        for option in self.optionList:
            option.image = pygame.Surface([spaceWidth*0.9,optionHeight*self.spaceHeightFactor])
            option.rect = option.image.get_rect()

            count = self.optionList.index(option)
            option.rect.x = 0
            option.rect.y = count*optionHeight

            # option.button = option.rect.inflate(-option.image.get_height()*0.2,-option.image.get_height()*0.2)
            # option.button.x = option.image.get_height()*0.1
            # option.button.y = option.image.get_height()*0.1

            #option.textPos =[(option.image.get_width()-option.printedName.get_width())*0.5,(option.image.get_height()-option.printedName.get_height())*0.5]
            option.textPos =[self.selector.rect.width + self.cursorToTextSpacing,(option.image.get_height()-option.printedName.get_height())*0.5]

    @property
    def isActivated(self):
        return self._isActivated

    @property
    def isActivated(self):
        return self._isActivated

    @isActivated.setter
    def isActivated(self, value):
        self._isActivated = value
        if value == True:
            self.chosenOptionIndex = None

    def notify(self, event):
        if self.isActivated:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.optionList[self.selector.selectedIndex].deselect()
                    self.selector.moveUp()
                    self.scrollUp()
                    self.optionList[self.selector.selectedIndex].select()
                elif event.key == pygame.K_DOWN:
                    self.optionList[self.selector.selectedIndex].deselect()
                    self.selector.moveDown()
                    self.scrollDown()
                    self.optionList[self.selector.selectedIndex].select()
                elif event.key == pygame.K_SPACE:
                    self.chosenOptionIndex = self.selectedIndex()
                    self.isActivated = False
                elif event.key == pygame.K_RETURN:
                    self.chosenOptionIndex = self.selectedIndex()
                    self.isActivated = False

    def scrollDown(self):
        if self.selectedIndex() > (self.displayedOptions -1) + self.scrolledPosition and self.scrolledPosition != (self.numberOfOptions - 1):
            self.scrolledPosition += 1
            for option in self.optionList:
                count = self.optionList.index(option)

    def scrollUp(self):
        if self.selectedIndex() < self.scrolledPosition and self.scrolledPosition != 0:
            self.scrolledPosition -= 1

    def update(self):
        for opt in self.optionList:
            opt.update()

        if not self.activated:
            self.optionList[self.selector.selectedIndex].deselect()
        else:
            self.optionList[self.selector.selectedIndex].select()

    def selectedIndex(self):
        return self.selector.selectedIndex

    def draw(self, screen):
        self.image.fill(WHITE)

        for i in range(self.scrolledPosition, self.displayedOptions+self.scrolledPosition):
            option = self.optionList[i]
            scrolledRect = pygame.Rect(option.rect.x, (i-self.scrolledPosition)*self.optionList[0].printedName.get_height(), option.rect.width, option.rect.height)
            self.image.blit(option.image, scrolledRect)

        # for option in self.spritesOptions.sprites():
        #     self.image.blit(option.image, option.rect)

        cursorPos = pygame.Rect(self.selectedOption().rect.x, self.selectedOption().rect.centery - self.scrolledPosition*self.optionList[0].printedName.get_height() - self.selector.rect.height/2, self.selectedOption().rect.width, self.selectedOption().rect.height)
        self.image.blit(self.selector.image, cursorPos)

        screen.blit(self.image, self.rect)

    def selectedOption(self):
        return self.optionList[self.selectedIndex()]