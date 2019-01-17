#-*- coding:utf-8 -*-
import pygame, sys, traceback, time
import myhero
import enemy
import door
from pygame.locals import *
import random



def main():
    pygame.init()
    pygame.mixer.init()
    bg_size = 1200, 800
    color_red = (255, 0, 0)
    color_green = (0, 255, 0)
    color_blue = (0, 0, 255)
    fullscreen = False
    def add_it(group1, group2, num):
        for i in range(num):
            e1 = enemy.Enemy(bg_size)
            group1.add(e1)
            group2.add(e1)

    def add_it2(group1, group2, num):
        for i in range(num):
            e2 = enemy.Enemy2(bg_size)
            group1.add(e2)
            group2.add(e2)

    def add_it3(group1, group2, num):
        for i in range(num):
            e3 = enemy.Enemy3(bg_size)
            group1.add(e3)
            group2.add(e3)

    background = pygame.image.load(
        'C:\\Users\\Administrator\\Desktop\\image\\3.png')
    #加载背景音乐
    pygame.mixer.music.load(
        "C:\\Users\\Administrator\\Desktop\\image\\bg_music1.mp3")
    pygame.mixer.music.set_volume(20)
    pygame.mixer.music.play()
    #设置定时器
    CLOCK = USEREVENT
    pygame.time.set_timer(CLOCK, 1000)
    #绘制屏幕框体
    screen = pygame.display.set_mode(bg_size, RESIZABLE)
    # 初始化计时器
    counts = 0
    #设置标题
    pygame.display.set_caption('生存者--survivor')

    #生成我方英雄
    me = myhero.MyHero(bg_size)
    #生成敌方怪物
    guai1=enemy.Enemy(bg_size)
    guai2=enemy.Enemy2(bg_size)
    guai3=enemy.Enemy3(bg_size)
    #生存怪物军队（组）
    enemies = pygame.sprite.Group()
    #生成传送门
    door1 = door.Door1(bg_size)
    door2 = door.Door2(bg_size)
    door3 = door.Door3(bg_size)
    door4 = door.Door4(bg_size)
    door5 = door.Door5(bg_size)
    # it = enemy.Enemy(bg_size)
    # it2 = enemy.Enemy2(bg_size)
    # it3 = enemy.Enemy3(bg_size)
    it = pygame.sprite.Group()
    it2 = pygame.sprite.Group()
    it3 = pygame.sprite.Group()
     
    add_it(it, enemies, 3)
    add_it2(it2, enemies, 3)
    add_it3(it3, enemies, 3)
    #设置字体对象
    fontObj = pygame.font.Font("C:\\Windows\\Fonts\\simhei.ttf", 25)
    fontObj2 = pygame.font.Font("C:\\Windows\\Fonts\\simhei.ttf", 80)
    clock = pygame.time.Clock()
    running = True
    #计时器
    
    while running:
        #写字
        blood=me.patient+me.intelligence+me.patient+me.stay_power+me.attention
        switch = True
            

        textSurfaceObj = fontObj.render('血量:', True, color_red)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (900, 30)
        textSurfaceObj2 = fontObj.render(str(blood), True, color_red)
        textRectObj2 = textSurfaceObj2.get_rect()
        textRectObj2.center = (960, 30)
        textSurfaceObj3 = fontObj.render('生存时间：', True, color_red)
        textRectObj3 = textSurfaceObj3.get_rect()
        textRectObj3.center = (750, 30)
        textSurfaceObj4 = fontObj2.render(str(counts), True, color_blue)
        textRectObj4 = textSurfaceObj4.get_rect()
        textRectObj4.center = (820, 30)
        textSurfaceObj7 = fontObj.render('力量:'+str(me.power), True, color_red)
        textRectObj7 = textSurfaceObj7.get_rect()
        textRectObj7.center = (960, 50)
        textSurfaceObj8 = fontObj.render('耐力:'+str(me.stay_power), True, color_red)
        textRectObj8 = textSurfaceObj8.get_rect()
        textRectObj8.center = (960, 70)
        textSurfaceObj9 = fontObj.render('注意力'+str(me.attention), True, color_red)
        textRectObj9 = textSurfaceObj9.get_rect()
        textRectObj9.center = (960, 90)
        textSurfaceObj10 = fontObj.render('智力:'+str(me.intelligence), True, color_red)
        textRectObj10 = textSurfaceObj10.get_rect()
        textRectObj10.center = (960, 110)
        textSurfaceObj11 = fontObj.render('耐心'+str(me.patient), True, color_red)
        textRectObj11 = textSurfaceObj11.get_rect()
        textRectObj11.center = (960, 130)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                bg_size = event.size
                width, height = bg_size
                screen = pygame.display.set_mode(bg_size, RESIZABLE)
            elif event.type == CLOCK:
                counts +=1
                
                #检测用户键盘操作
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_UP]:
            me.moveup()
        elif key_pressed[K_DOWN]:
            me.movedown()
        elif key_pressed[K_LEFT]:
            me.moveleft()
        elif key_pressed[K_RIGHT]:
            me.moveright()
        elif key_pressed[K_F11]:
            fullscreen = not fullscreen
            if fullscreen:
                screen = pygame.display.set_mode((1920, 1080),
                                                 FULLSCREEN | HWSURFACE)
            else:
                screen = pygame.display.set_mode(bg_size, RESIZABLE)


#        绘制背景
        screen.blit(background, (0, 0))
        
        #绘制文字
        screen.blit(textSurfaceObj, textRectObj)
        for i in range(2,12):
            if i==5 or i == 6:
                pass
            else:
                screen.blit(eval('textSurfaceObj'+str(i)), eval('textRectObj'+str(i)))
        #绘制我方英雄
        # switch_image = not switch_image
        # if switch_image :
        screen.blit(me.image, me.rect)
        #绘制传送门
        for i in range(1,6):
            screen.blit(eval('door'+str(i)+'.image'), eval('door'+str(i)+'.rect'))

        if(blood<=0):
            
            pygame.mixer.music.stop()
            counts2=counts
            pygame.time.set_timer(CLOCK,0)
            textSurfaceObj5 = fontObj.render('你的生存时间为:', True, color_red)
            textRectObj5 = textSurfaceObj5.get_rect()
            textRectObj5.center = (420, 400)
            textSurfaceObj6= fontObj.render(str(counts2)+'秒'+"   5秒后退出游戏", True, color_red)
            textRectObj6 = textSurfaceObj6.get_rect()
            textRectObj6.center = (650, 400)
            screen.blit(textSurfaceObj5, textRectObj5)
            screen.blit(textSurfaceObj6, textRectObj6)
            pygame.display.flip()
            clock.tick(60)
            time.sleep(5)
            pygame.quit()
            sys.exit()
        # else:
        #     screen.blit(me.image2, me.rect)
        #绘制怪物
        for each in it:
            each.move()
            if each.active:
                screen.blit(each.image, each.rect)
            else:
                each.reset()

        for each in it2:
            each.move()
            if each.active:
                screen.blit(each.image, each.rect)
            else:
                each.reset()
        for each in it3:
            each.move()
            if each.active:
                screen.blit(each.image, each.rect)
            else:
                each.reset()
        # screen.blit(it3.image,it.rect)
        #碰撞检测：
        enemies_it_down = pygame.sprite.spritecollide(\
        me, it,True,pygame.sprite.collide_mask)
        enemies_it2_down = pygame.sprite.spritecollide(\
        me, it2,True,pygame.sprite.collide_mask)
        enemies_it3_down = pygame.sprite.spritecollide(\
        me, it3,True,pygame.sprite.collide_mask)
        door1_down = pygame.sprite.collide_rect(\
        me, door1)
        door2_down = pygame.sprite.collide_rect(\
        me, door2)
        door3_down = pygame.sprite.collide_rect(\
        me, door3)
        door4_down = pygame.sprite.collide_rect(\
        me, door4)
        door5_down = pygame.sprite.collide_rect(\
        me, door5)
        
        if enemies_it_down:
            #掉一滴血
            me.power+= 1
            me.stay_power+=1
            me.attention+=1
            me.patient +=1
            me.intelligence+=1
            print('碰到小怪掉了10滴血')
            for i in enemies_it_down:
                i.active = False
            # it = pygame.sprite.Group()
            # it2 = pygame.sprite.Group()
            # it3 = pygame.sprite.Group()
             
            num = random.randint(0, 3)
            num2 = random.randint(1, 3)
            if num == 0:
                add_it(it, enemies, num2)
            elif num == 1:
                add_it2(it2, enemies, num2+1)
            elif num == 2:
                add_it3(it3, enemies, num2)
            for each in it:
                if each.active:
                    screen.blit(each.image, each.rect)
                else:
                    each.reset()

            for each in it2:
                
                if each.active:
                    screen.blit(each.image, each.rect)
                else:
                    each.reset()
            for each in it3:
                if each.active:
                    screen.blit(each.image, each.rect)
                else:
                    each.reset()
        elif enemies_it2_down:
            #掉一滴血
            me.power-=2
            me.stay_power-=3
            me.attention-=3
            me.patient -=2
            me.intelligence-=2
            print('碰到中怪掉了20滴血')
            for i in enemies_it2_down:
                i.active = False
            # it = pygame.sprite.Group()
            # it2 = pygame.sprite.Group()
            # it3 = pygame.sprite.Group()
             
            num = random.randint(0, 3)
            num2 = random.randint(0, 3)
            if num == 0:
                add_it(it, enemies, num2)
            elif num == 1:
                add_it2(it2, enemies, num2)
            elif num == 2:
                add_it3(it3, enemies, num2)
            for each in it:
                if each.active:
                    screen.blit(each.image, each.rect)
                else:
                    each.reset()

            for each in it2:
                if each.active:
                    screen.blit(each.image, each.rect)
                else:
                    each.reset()
            for each in it3:
                if each.active:
                    screen.blit(each.image, each.rect)
                else:
                    each.reset()
        if enemies_it3_down:
            me.speed+=1
            me.power +=1
            me.stay_power+=1
            me.attention+=1
            me.patient +=1
            me.intelligence+=1
            #掉一滴血
            for i in enemies_it3_down:
                i.active = False
            # it = pygame.sprite.Group()
            # it2 = pygame.sprite.Group()
            # it3 = pygame.sprite.Group()
             
            num = random.randint(0, 3)
            num2 = random.randint(0, 3)
            if num == 0:
                add_it(it, enemies, num2)
            elif num == 1:
                add_it2(it2, enemies, num2+1)
            elif num == 2:
                add_it3(it3, enemies, num2)
            for each in it:
                if each.active:
                    screen.blit(each.image, each.rect)
                else:
                    each.reset()

            for each in it2:
                if each.active:
                    screen.blit(each.image, each.rect)
                else:
                    each.reset()
            for each in it3:
                if each.active:
                    screen.blit(each.image, each.rect)
                else:
                    each.reset()
        elif door1_down:
            background = pygame.image.load(
                'C:\\Users\\Administrator\\Desktop\\image\\1.png')
            
            # print('遇见传送门')
        elif door2_down:
            background = pygame.image.load(
                'C:\\Users\\Administrator\\Desktop\\image\\2.png')
            
            # print('遇见传送门')
        elif door3_down:
            background = pygame.image.load(
                'C:\\Users\\Administrator\\Desktop\\image\\3.png')
            # print('遇见传送门')
        elif door4_down:
            background = pygame.image.load(
                'C:\\Users\\Administrator\\Desktop\\image\\4.png')
            
            # print('遇见传送门')
        elif door5_down:
            background = pygame.image.load(
                'C:\\Users\\Administrator\\Desktop\\image\\5.png')
            
            # print('遇见传送门')
        # print(me.speed, me.stay_power, me.patient, me.power, me.attention,
        #       me.intelligence)
        if switch:
            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()