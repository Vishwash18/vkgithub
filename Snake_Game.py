import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows=0
    w=0
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        pass
    def move(self,dirnx,dirny):
        pass
    def draw(self,surface,eyes=False):
        pass
class snake(object):

    def __init__(self,color,pos):
        pass
    def move(self):
        pass
    def reset(self,pos):
        pass
    def addcube(self):
        pass
    def draw(self,surface):
        pass
def drawGrid(w,row,surface):
    sizeBtwn=w//rows
    x=0
    y=0
    for l in range(rows):
        x=x+sizeBtwn
        y=y+sizeBtwn
        pygame.draw.line(surface,(255,255,255),(x,0),(x,w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))
def redrawWindow(surface):
    global rows,width
    surface.fill((0,0,0))
    drawGrid(width,rows,surface)
    pygame.display.update()
def message_box(subject,content):
    pass
def main():
    global width,rows
    width=500
    rows=20
    win=pygame.display.set_mode((width,width))
    s=snake((255,0,0),(10,10))
    flag=True
    clock=pygame.time.clock()
    while flag:
        pygame.time.delay(50)
        clock.time(10)
        redrawWindow(win)
    pass