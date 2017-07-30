import pygame
from app.settings import *


class PlayerDeadFadeOut():
    def __init__(self, screen):
        fontScreen = pygame.font.Font(FONT_NAME, 40)
        message = fontScreen.render("YOU'RE DOWN", True, LIFE_BAR_COLOR)
        message2 = fontScreen.render("BUT DON'T GIVE UP!", True, LIFE_BAR_COLOR)
        messagePos = [(SCREEN_WIDTH - message.get_width()) / 2,
                      (SCREEN_HEIGHT - message.get_height()) / 3]
        messagePos2 = [(SCREEN_WIDTH - message.get_width() * 1.75),
                      ((SCREEN_HEIGHT - message.get_height()) / 3) * 2]

        for i in range(100):
            fadeInSurface = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
            fadeInSurface.fill(BLACK)
            fadeInSurface.set_alpha(i)
            screen.blit(fadeInSurface, (0, 0))
            if message != None:
                screen.blit(message, messagePos)
                screen.blit(message2, messagePos2)
            pygame.time.wait(15)
            pygame.display.flip()
        pygame.time.wait(60)