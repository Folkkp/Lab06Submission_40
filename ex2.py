import sys 
import pygame as pg
pg.init()

class Rectangle:
    def __init__(self,x = 0,y = 0,w = 0,h = 0,r = 0,g = 0,b = 0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.R = r
        self.G = g
        self.B = b
    def draw(self,screen):
        pg.draw.rect(screen,(self.R,self.G,self.B),(self.x,self.y,self.w,self.h))
        
win_x = 800
win_y = 480
screen = pg.display.set_mode((win_x, win_y))
key_w = False
key_a = False
key_s = False
key_d = False
w = 0
a = 0
s = 0
d = 0
posX , posY = 50,50
while(True):
    screen.fill((255,255,255))
    pg.draw.rect(screen,(254,200,216),(posX -a +d,posY -w +s ,100,100))
    if key_w:
        w += 1
    if key_a:
        a += 1
    if key_s:
        s += 1
    if key_d:
        d += 1
    
    pg.display.update()
    pg.time.delay(3)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_w :
            key_w = True
        if event.type == pg.KEYUP and event.key == pg.K_w :
            key_w = False
            
        if event.type == pg.KEYDOWN and event.key == pg.K_a :
            key_a = True
        if event.type == pg.KEYUP and event.key == pg.K_a :
            key_a = False
            
        if event.type == pg.KEYDOWN and event.key == pg.K_s :
            key_s = True
        if event.type == pg.KEYUP and event.key == pg.K_s :
            key_s = False
            
        if event.type == pg.KEYDOWN and event.key == pg.K_d :
            key_d = True
        if event.type == pg.KEYUP and event.key == pg.K_d :
            key_d = False
            
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        