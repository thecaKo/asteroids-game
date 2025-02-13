import pygame
import asteroidfield
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)


    player = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        dt = clock.tick(60) / 1000
        
        updatable.update(dt)
        pygame.Surface.fill(screen, color="black")
        
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()  
