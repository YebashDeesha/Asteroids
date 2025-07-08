import pygame
from constants import *
import sys
from player import *
from circleshape import *
from asteroid import Asteroid
from asteroidfield import *
from shoot import Shoot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    
    Asteroid.containers = (asteroids, updatable, drawable)
    Shoot.containers = (shoots, updatable, drawable)
    asteroid_field = pygame.sprite.Group()
    AsteroidField.containers = (updatable)

    Player.containers = (updatable, drawable)
    asterteroids_field = AsteroidField()
    dt = 0
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for a in asteroids:
            if a.colision(player):
                print("Game over!")
                sys.exit()
        for a in asteroids:
            for s in shoots:
                if a.colision(s):
                    a.kill()
                    s.kill()
                    


        screen.fill("black")

        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        

        dt = clock.tick(60) / 1000
  


if __name__ == "__main__":
    main()
