import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        pygame.Surface.fill(screen, color="black")
        pygame.display.flip()



if __name__ == "__main__":
    main()  
