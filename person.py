import pygame
import time
import math
import fractions
jumpcount = 10


class Character(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        self.rect = self.image.get_rect()
        self.isFinished = False
        self.isJump = False

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 690:
            self.rect.x = 690

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def Jump(self):
        global jumpcount
        if jumpcount >= -10:
            self.isJump = True
            self.isFinished = False
            pygame.time.delay(1)
            neg = 1
            if jumpcount < 0:
                neg = -1
            self.rect.y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount = jumpcount - 1
            if self.rect.y == 480 or self.rect.y > 480:
                self.rect.y = 480
        else:
            jumpcount = 10
            self.isJump = False
            self.isFinished = True







