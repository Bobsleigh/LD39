__author__ = 'Bobsleigh'


class Animation:
    def __init__(self, imageList, delay,infiniteLoop = False):

        self.imageList = imageList
        self.delay = delay
        self.infiniteLoop = infiniteLoop
        self.isRunning = False
        self.timer = 0
        self.currentImage = imageList[0]
        self.defaultImage = imageList[0]
        self.timerMax = delay * len(self.imageList)

    def update(self):
        if (self.infiniteLoop):
            self.startInfinite()

        if self.isRunning:
            if self.timer < self.timerMax:
                self.currentImage = self.imageList[self.timer//self.delay]
                self.timer += 1
                return self.currentImage
            else:
                if self.infiniteLoop:
                    self.timer = 0
                else:
                    self.stop()
            return self.defaultImage

        else:
            return self.defaultImage

    def start(self):
        self.isRunning = True


    def startInfinite(self):
        self.infiniteLoop = True
        self.isRunning = True

    def stop(self):
        self.infiniteLoop = True
        self.isRunning = False
        self.timer = 0



