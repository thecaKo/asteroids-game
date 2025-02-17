import pygame
import asteroidfield
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from sys import exit

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shoot.containers = (updatable, drawable, shoots)


    player = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField() 

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        dt = clock.tick(60) / 1000  

        updatable.update(dt)

        for ast in asteroids:
            if ast.collisions(player) == True:
                print("Game Over!")
                exit()

        screen.fill((0, 0, 0))

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()  
