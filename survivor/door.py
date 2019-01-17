import pygame
from random import *
class Door1(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\d1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # self.image2 = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\guanyu2.gif").convert_alpha()
        self.rect.left,self.rect.top = 0,0
        self.active = True
class Door2(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\d2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # self.image2 = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\guanyu2.gif").convert_alpha()
        self.rect.left,self.rect.top = 1100,0
        self.active = True
class Door3(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\d3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # self.image2 = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\guanyu2.gif").convert_alpha()
        self.rect.left,self.rect.top = 0,675
        self.active = True
class Door4(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\d4.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # self.image2 = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\guanyu2.gif").convert_alpha()
        self.rect.left,self.rect.top = 1100,675
        self.active = True
class Door5(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\d5.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # self.image2 = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\guanyu2.gif").convert_alpha()
        self.rect.left,self.rect.top = 600,400
        self.active = True