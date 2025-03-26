import pygame
import math as m

w=600
h=500
tx1 = 0
ty1 = h
tx2 = w-400
ty2 = h
tx3 = 0
ty3 = h-300
trangle_points = [(tx1, ty1), (tx2, ty2), (tx3, ty3)]

screen = pygame.display.set_mode((600, 500))
screen.fill((255, 255, 255))
pygame.display.set_caption("Draw a trangle")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.polygon(screen, (255, 0, 0), trangle_points, 2)
    pygame.display.flip()
pygame.quit()