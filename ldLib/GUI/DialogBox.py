__author__ = 'Bobsleigh'
import pygame

from app.settings import *
from ldLib.GUI.WrappedTextBox import WrappedTextBox


class DialogBox(pygame.sprite.Sprite):
    def __init__(self,pos, size, text, margin=(10,10)):
        super().__init__()

        self.textBox = WrappedTextBox(pos, size, text, margin)

        self.image = self.textBox.image
        self.rect = self.textBox.rect

        self._isActivated = True
        self._notifyGroup = None

    @property
    def isActivated(self):
        return self._isActivated

    @property
    def isActivated(self):
        return self._isActivated

    @isActivated.setter
    def isActivated(self, value):
        self._isActivated = value

    def notify(self, event):
        if self.isActivated:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_SPACE:
                    self.isActivated = False
                elif event.key == pygame.K_RETURN:
                    pass

    def kill(self):
        self._notifyGroup.remove(self)
        super().kill()

    def update(self):
        if not self.isActivated:
            self.kill()
