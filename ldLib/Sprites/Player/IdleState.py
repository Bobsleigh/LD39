__author__ = 'Bobsleigh'

import pygame
from ldLib.Sprites.Player.PlayerState import PlayerState
from app.settings import *

class IdleState(PlayerState):
    def __init__(self):
        super().__init__()

    def handleInput(self, sprite, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                sprite.updateSpeedRight()
                sprite.rightPressed = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                sprite.updateSpeedLeft()
                sprite.leftPressed = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                sprite.updateSpeedDown()
                sprite.downPressed = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                sprite.updateSpeedUp()
                sprite.upPressed = True
            elif event.key == pygame.K_LSHIFT:
                sprite.leftShiftPressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                sprite.rightPressed = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                sprite.leftPressed = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                sprite.upPressed = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                sprite.downPressed = False
            elif event.key == pygame.K_LSHIFT:
                sprite.leftShiftPressed = False
            elif event.key == pygame.K_SPACE:
                sprite.spacePressed = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_LEFT:
                sprite.leftMousePressed = True
            elif event.button == MOUSE_RIGHT:
                sprite.rightMousePressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == MOUSE_LEFT:
                sprite.leftMousePressed = False
            elif event.button == MOUSE_RIGHT:
                sprite.rightMousePressed = False

    def enter(self, sprite):
        pass

    def exit(self, sprite):
        pass