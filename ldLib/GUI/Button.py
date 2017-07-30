import pygame
from app.settings import *

class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size, text, callback):
        super().__init__()

        self.method = callback

        self.fontSize = 24
        self.buttonFont = pygame.font.Font(FONT_NAME, self.fontSize)

        self.width = size[0]
        self.height = size[1]

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.borderButton = 5

        self.interior = pygame.Rect(self.borderButton, self.borderButton, self.width - 2 * self.borderButton,
                                    self.height - 2 * self.borderButton)
        self.text = text

        self.textPos = [0, 0]

        self.isSelected = False

        # Color
        self.color1 = COLOR_MENU_1
        self.color2 = COLOR_MENU_2

    def doNothing(self):
        print('You did nothing')

    def update(self):

        if self.isSelected:
            self.color1 = COLOR_MENU_SELECT_1
            self.color2 = COLOR_MENU_SELECT_2
            self.printedText = self.buttonFont.render(self.text, True, COLOR_MENU_FONTS_SELECT)

        else:
            self.color1 = COLOR_MENU_1
            self.color2 = COLOR_MENU_2
            self.printedText = self.buttonFont.render(self.text, True, COLOR_MENU_FONTS)

        self.setUpgradeSpec()

        self.image.fill(self.color2)
        self.image.fill(self.color1, self.interior)
        self.image.blit(self.printedText, self.textPos)

    def setUpgradeSpec(self):
        self.textPos = [(self.image.get_width() - self.printedText.get_width()) / 2,
                        (self.image.get_height() - self.printedText.get_height()) / 2]


    def notify(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_LEFT:
                if self.rect.collidepoint(event.pos):
                    self.method()