__author__ = 'Bobsleigh'
import pygame

from app.settings import *

class Animation:
    def __init__(self, imageList, delay, direction = LEFT, infiniteLoop = False):

        self.imageListLeft = imageList
        self.imageListRight = list()
        for item in imageList:
            self.imageListRight.append(pygame.transform.flip(item, True, False))

        if (direction == RIGHT):
            # Swap image
            self.imageListLeft, self.imageListRight = self.imageListRight,self.imageListLeft

        self.delay = delay
        self.infiniteLoop = infiniteLoop
        self.isRunning = False
        self.timer = 0
        self.currentImage = imageList[0]
        self.timerMax = delay * len(self.imageListLeft)

    def update(self, direction=LEFT):
        # Select direction
        imageList = self.imageListLeft
        if direction == RIGHT:
            imageList=self.imageListRight

        self.startInfinite()
        if self.isRunning:
            if self.timer < self.timerMax:
                self.currentImage = imageList[self.timer//self.delay]
                self.timer += 1
                return self.currentImage
            else:
                if self.infiniteLoop:
                    self.timer = 0
                else:
                    self.stop()
            return imageList[0]

        else:
            return imageList[0]

    def start(self):
        self.isRunning = True

    def startInfinite(self):
        self.infiniteLoop = True
        self.isRunning = True

    def stop(self):
        self.infiniteLoop = True
        self.isRunning = False
        self.timer = 0



