#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:11:38 2021

@author: pszit
"""
# library import

import pygame as pg

#define your global variables
WIDTH = 800
HEIGHT = 600
BORDER = 40

pg.init()

screen = pg.display.set_mode((WIDTH,HEIGHT))

# defining background and foreground colours
bg_color = pg.Color("blue")
fg_color = pg.Color("grey")

# filling the screen with background colour
screen.fill(bg_color)

# drawing the walls
pg.draw.rect(screen,fg_color,pg.Rect(0,0,WIDTH,BORDER))
pg.draw.rect(screen,fg_color,pg.Rect(0,0,BORDER,HEIGHT))
pg.draw.rect(screen,fg_color,pg.Rect(0,HEIGHT-BORDER-1,WIDTH,BORDER))

# flipping the changes to the screen
pg.display.flip()

# waiting for the user to interact with the game
while True:
    e = pg.event.poll()
    if e.type == pg.QUIT:
        break
# quitting/closing the game
pg.quit()
