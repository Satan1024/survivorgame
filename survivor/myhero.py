#-*- coding:utf-8 -*-
import pygame


class MyHero(pygame.sprite.Sprite):
    

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "C:\\Users\\Administrator\\Desktop\\image\\wangsicong.png"
        ).convert_alpha()
        # self.image2 = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\guanyu2.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = 0,200
        self.width, self.height = bg_size[0], bg_size[1]
        
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        self.power = 20.0
        self.stay_power = 20.0
        self.intelligence = 20.0
        self.patient = 20.0
        self.attention = 20.0
        self.speed = 50

    def moveup(self):
        self.active = True
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def movedown(self):
        self.active = True
        if self.rect.bottom < self.height:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height

    def moveleft(self):
        self.active = True
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveright(self):
        self.active = True
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width
