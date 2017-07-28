__author__ = 'Bobsleigh'

class Cooldown:
    def __init__(self, maximum):
        self.max = maximum
        self.value = 0
        self.isZero = True

    def update(self):
        if not self.isZero:
            self.value -= 1

            if self.value <= 0:
                self.value = 0
                self.isZero = True

    def start(self):
        self.value = self.max
        self.isZero = False