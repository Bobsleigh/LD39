__author__ = 'Bobsleigh'

import weakref

class NotifyGroup(weakref.WeakSet):
    def __init__(self):
        super().__init__()

    def add(self, item):
        item._notifyGroup = self
        super().add(item)

    def remove(self, item):
        item._notifyGroup = None
        super().remove(item)