import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT / 2)

    while True:
        # Handle events first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        dt = clock.tick(60) / 1000
        
        # Update game state
        player.update(dt)  # Add this line!
        
        # Draw everything
        pygame.Surface.fill(screen, color="black")
        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()  
