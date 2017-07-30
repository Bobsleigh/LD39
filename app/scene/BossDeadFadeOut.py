import pygame
from app.settings import *


class BossDeadFadeOut():
    def __init__(self, screen):
        fontScreen = pygame.font.SysFont(FONT_NAME, 40)
        message = fontScreen.render("Congratulations!", True, (0, 0, 0))
        messagePos = [(SCREEN_WIDTH - message.get_width()) / 2,
                      (SCREEN_HEIGHT - message.get_height()) / 2]

        for i in range(100):
            fadeInSurface = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
            fadeInSurface.fill(BLACK)
            fadeInSurface.set_alpha(i)
            screen.blit(fadeInSurface, (0, 0))
            if message != None:
                screen.blit(message, messagePos)
            pygame.time.wait(15)
            pygame.display.flip()
        pygame.time.wait(60)