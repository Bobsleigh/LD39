import pygame

from app.settings import *
from ldLib.GUI.Box import Box


class WrappedTextBox(pygame.sprite.Sprite):
    def __init__(self,pos, size, text, margin=(10,10)):
        super().__init__()

        self.marginX = margin[0]
        self.marginY = margin[1]
        self.spaceBetweenLines = 20

        self.box = Box(pos,size)

        self.image = self.box.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.arial = pygame.font.SysFont("Arial", DIALOG_TEXT_SIZE)
        self.text = self.renderWrappedText(text)

    def isTextLongerThanBox(self, renderedTxt):
        txtRect = renderedTxt.get_rect()
        if txtRect.width + self.marginX * 2 > self.rect.width:
            return True
        else:
            return False

    def isTextLongerThanBoxNEW(self, text):
        textSize = self.arial.size(text)
        if textSize[0] + self.marginX * 2 > self.rect.width:
            return True
        else:
            return False

    def getWrappedLineList(self,text):
        line = ""
        lastLine = ""
        lineList = []
        renderList = []

        if self.isTextLongerThanBox(self.arial.render(text, False, BLACK)):
            wordList = text.split(" ")
            for word in wordList:
                lastLine = line
                line += (" " + word)
                render = self.arial.render(line, False, BLACK)

                if self.isTextLongerThanBox(render):
                    lineList.append(lastLine.lstrip())
                    lastWord = line.split(" ")[-1]
                    line = lastWord

            lineList.append(line.lstrip())

            return lineList

        else:
            lineList.append(text)
            return lineList

    def renderWrappedText(self, text):
        lineList = self.getWrappedLineList(text)
        i = 0

        while i < len(lineList):
            renderSize = self.arial.size(lineList[i])
            render = self.arial.render(lineList[i], False, BLACK)
            if i == 0:
                self.box.box.blit(render, (self.marginX,self.marginY))
            else:
                self.box.box.blit(render, (self.marginX,self.marginY + (self.spaceBetweenLines + renderSize[1]) * (i)))
            i += 1




