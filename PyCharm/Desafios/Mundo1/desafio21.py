import Pygame
# faca um programa em python que abra e reproduza o audio de um arqiovo MP3
pygame.init()
pygame.mixer.music.load('quebramar.mp3')
pygame.mixer.music.play()
pygame.event.wait()
