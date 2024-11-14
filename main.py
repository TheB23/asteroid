import pygame
import sys
from asteroidField import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    
    # Creating the group for Player Class from pygame
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Creating the group for Astroid
    Asteroid.containers = (asteroids, updatable, drawable)
    # Creating the Asteroid fields setup
    AsteroidField.containers = (updatable,)
    asteroid_filed = AsteroidField()

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        for act in updatable:
            act.update(dt)
            
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("game over!!")
                sys.exit()
        
        for shape in drawable:
            shape.draw(screen)
        
        pygame.display.flip() 

if __name__ == "__main__":
    main()
