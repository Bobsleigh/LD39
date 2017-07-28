class Selector():
    def __init__(self,num):
        #Default position
        self.hPos = 0
        self.vPos = 0
        self.maxOpt = num

    def moveRight(self):
        pass

    def moveLeft(self):
        pass

    def moveUp(self):
        if self.vPos > 0:
            self.vPos += -1
        elif self.vPos == 0:
            self.vPos = self.maxOpt-1

    def moveDown(self):
        if self.vPos < self.maxOpt-1:
            self.vPos += 1
        elif self.vPos == self.maxOpt-1:
            self.vPos = 0