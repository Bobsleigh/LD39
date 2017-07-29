__author__ = 'Bobsleigh'

class EnemyState:
    def __init__(self):
        pass

    def update(self, sprite, mapData):
        raise NotImplementedError('Subclasses must override handleInput()')

    def enter(self, sprite):
        raise NotImplementedError('Subclasses must override enter()')

    def exit(self, sprite):
        raise NotImplementedError('Subclasses must override exit()')