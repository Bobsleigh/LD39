import pygame
from app.settings import *


class BossDeadFadeOut():
    def __init__(self, screen):

        for i in range(100):
            fadeInSurface = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
            fadeInSurface.fill(BLACK)
            fadeInSurface.set_alpha(i)
            screen.blit(fadeInSurface, (0, 0))
            if i < 50:
                pygame.time.wait(60)
            else:
                pygame.time.wait(10)
            pygame.display.flip()
        pygame.time.wait(60)