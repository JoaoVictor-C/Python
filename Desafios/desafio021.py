import pygame
pygame.mixer.init()
pygame.mixer.music.load('d:\JV\Meus Projetos\Python\Desafios\ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()