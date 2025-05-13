import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from constants import *
from shoot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    dt: float = 0
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        dt = clock.tick(60) / 1000
        for u in updatable:
            u.update(dt)

        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game over!")
                return
            for shot in shots:
                if shot.colliding(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.Surface.fill(screen, color="black")
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
