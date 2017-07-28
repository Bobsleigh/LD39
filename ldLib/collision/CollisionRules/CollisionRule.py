__author__ = 'Bobsleigh'

class CollisionRule:
    def __init__(self):
        pass

    def onMoveX(self, sprite):
        raise NotImplementedError('Subclasses must override enter()')

    def onMoveY(self, sprite):
        raise NotImplementedError('Subclasses must override enter()')