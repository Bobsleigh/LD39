import pygame, os

class MusicHandler:
    def __init__(self, gameData):
        self.gameData = gameData
        self.sceneData = gameData.sceneData
        self.musicName = self.sceneData.musicName

    def play(self):
        if self.musicName == "BoxCat_Games_-_25_-_Victory.wav": # Hack
            pygame.mixer.music.load(os.path.join('music', self.musicName))
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.load(os.path.join('music', self.musicName))
            pygame.mixer.music.set_volume(0.80)
            pygame.mixer.music.play(-1)

    def stop(self):
        pygame.mixer.music.stop()
