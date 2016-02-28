#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import * 



pygame.init()
tamX = 500
tamY = 600
ventana = pygame.display.set_mode((tamX,tamY))
pygame.display.set_caption("Práctica 9")

Color = (51, 102, 153)
incX = 1
incY = 1
posX = 100
posY = 250
imagenFondo = pygame.image.load("tux.png")
continuar = True
while continuar:
	posY += incY
	if posY+256 > tamY or posY < 0:
		incY *= -1
	posX += incX
	if posX+256 > tamX or posX < 0:
		incX *= -1
	ventana.fill(Color)	
	ventana.blit(imagenFondo,(posX,posY))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			continuar = False

	