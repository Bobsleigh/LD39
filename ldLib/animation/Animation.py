__author__ = 'Bobsleigh'


class Animation:
    def __init__(self, image, imageList, delay):

        self.imageList = imageList
        self.delay = delay
        self.timer = 0
        self.currentImage = image
        self.defaultImage = image
        self.isRunning = False

        self.timerMax = delay * len(self.imageList)

    def update(self):
        if self.isRunning:
            if self.timer < self.timerMax:
                self.currentImage = self.imageList[self.timer//self.delay]
                self.timer += 1
                return self.currentImage
            else:
                self.stop()
                return self.defaultImage
        else:
            return self.defaultImage

    def start(self):
        self.isRunning = True

    def stop(self):
        self.isRunning = False
        self.timer = 0



