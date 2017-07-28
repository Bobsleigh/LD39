class Animation():
    def __init__(self, sprite, frames, timer):
        self.frames = frames
        self.maxFrame = len(frames)
        self.timer = timer
        self.currentTimer = 0
        self.currentFrame = 0
        sprite.image = frames[self.currentFrame]


    def update(self, sprite):
        self.currentTimer += 1
        if self.currentTimer >= self.timer:
            self.currentFrame = (self.currentFrame+1) % (self.maxFrame)
            self.currentTimer = 0
            sprite.image = self.frames[self.currentFrame]

    def setAnimation(self,frames,timer):
        self.frames = frames
        self.maxFrame = len(frames)
        self.timer = timer