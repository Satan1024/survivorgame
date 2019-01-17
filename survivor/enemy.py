import pygame
from random import *
class Enemy(pygame.sprite.Sprite):
    power = 10.0
    stay_power = 10.0
    intelligence = 10.0
    patient = 10.0
    attention = 10.0
    blood = 50.0
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\6.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 10
        
        # self.image2 = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\guanyu2.gif").convert_alpha()
        self.rect.left,self.rect.top = randint(0,self.width -self.rect.width),randint(0,self.height - self.rect.height)
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        # self.speed = 20
    def reset(self):
        self.rect.left , self.rect.top = randint(0,self.width -self.rect.width),randint(0,self.height - self.rect.height)
    def move(self):
        # print('横坐标',self.rect.top,'纵坐标',self.rect.left)
        # print('self.height',self.height,'self.width',self.width)
        if self.rect.bottom<self.height and self.rect.top>0 and self.rect.left>0 and self.rect.right< self.width:
            # print('执行一次')
            c = randint(0,4)
            if c ==0 :
                self.rect.top +=self.speed
            elif c==1:
                self.rect.top -=self.speed
            elif c==2:
                self.rect.left +=self.speed
            elif c==3:
                self.rect.left -=self.speed
        else:
            print('又重置了')
            self.reset()



class Enemy2(pygame.sprite.Sprite):
    power = 20.0
    stay_power = 20.0
    intelligence = 20.0
    patient = 20.0
    attention = 20.0
    blood = 100.0

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\僵尸.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        # self.image2 = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\guanyu2.gif").convert_alpha()
        self.rect.left,self.rect.top = randint(0,self.width -self.rect.width),randint(0,self.height - self.rect.height)
        self.speed = 70
    def reset(self):
        self.rect.left , self.rect.top = randint(0,self.width -self.rect.width),randint(0,self.height - self.rect.height)
    def move(self):
        # print('横坐标',self.rect.top,'纵坐标',self.rect.left)
        # print('self.height',self.height,'self.width',self.width)
        if self.rect.bottom<self.height and self.rect.top>0 and self.rect.left>0 and self.rect.right< self.width:
            # print('执行一次')
            c = randint(0,4)
            if c ==0 :
                self.rect.top +=self.speed
            elif c==1:
                self.rect.top -=self.speed
            elif c==2:
                self.rect.left +=self.speed
            elif c==3:
                self.rect.left -=self.speed
        else:
            # print('又重置了')
            self.reset()

class Enemy3(pygame.sprite.Sprite):
    power = 20.0
    stay_power = 20.0
    intelligence = 20.0
    patient = 20.0
    attention = 20.0
    blood = 100.0

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\怪物石头.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)
        # self.image2 = pygame.image.load("C:\\Users\\Administrator\\Desktop\\image\\guanyu2.gif").convert_alpha()
        self.rect.left,self.rect.top = randint(0,self.width -self.rect.width),randint(0,self.height - self.rect.height)
        self.speed = 40
    def reset(self):
        self.rect.left , self.rect.top = randint(0,self.width -self.rect.width),randint(0,self.height - self.rect.height)
    def move(self):
        # print('横坐标',self.rect.top,'纵坐标',self.rect.left)
        # print('self.height',self.height,'self.width',self.width)
        if self.rect.bottom<self.height and self.rect.top>0 and self.rect.left>0 and self.rect.right< self.width:
            # print('执行一次')
            c = randint(0,4)
            if c ==0 :
                self.rect.top +=self.speed
            elif c==1:
                self.rect.top -=self.speed
            elif c==2:
                self.rect.left +=self.speed
            elif c==3:
                self.rect.left -=self.speed
        else:
            # print('又重置了')
            self.reset()
