#juego de la vida con pygame
import pygame
import random
import time

#definimos el tamaño de la pantalla
ancho = 800
alto = 600

#ejecutamos el metodo init()
pygame.init()

#cramos la pantalla 
pantalla = pygame.display.set_mode((ancho,alto))

#le damos color a la pantalla
pantalla.fill((255,255,255))

#hacemos que se mantenga abierta la pantalla
pygame.display.flip()

#for para que cambie de color el fondo 
for i in range(1,1000):
    #cambiamos el color de fondo
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pantalla.fill(color)
    #actualizamos la pantalla
    pygame.display.flip()
    #dormimos el programa
    time.sleep(0.01)

    
