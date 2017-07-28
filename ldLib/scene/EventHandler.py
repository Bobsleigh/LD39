import pygame
import sys

class EventHandler():
    def __init__(self):
        self.menuPause = None

    def eventHandle(self,notifySet):
        self.notifySet = notifySet
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            for obj in self.notifySet:
                obj.notify(event)