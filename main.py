import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Creating the group Class from pygame
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers() = (updatable, drawable)


    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = clock.tick(60) / 1000

        player.draw(screen)
        player.update(dt)

        pygame.display.flip() 

if __name__ == "__main__":
    main()
