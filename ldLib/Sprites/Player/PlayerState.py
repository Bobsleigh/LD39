__author__ = 'Bobsleigh'

class PlayerState:
    def __init__(self):
        pass

    def handleInput(self, sprite, event):
        raise NotImplementedError('Subclasses must override handleInput()')

    def enter(self, sprite):
        raise NotImplementedError('Subclasses must override enter()')

    def exit(self, sprite):
        raise NotImplementedError('Subclasses must override exit()')