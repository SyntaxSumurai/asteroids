import pygame
from constants import *
from player import Player,Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # make these groups the default containers for all sprites
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, bullets)

    # initialize screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}, height: {SCREEN_HEIGHT}")

    # create player -> automatically added to both groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    print("AsteroidField created:", asteroidField)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update first
        updatable.update(dt)

        for asteroid in asteroids:
            if not asteroid.checkCollision(player):
                print("Game over!")
                exit()

            for bullet in bullets:
                if not asteroid.checkCollision(bullet):
                    bullet.kill()
                    asteroid.split()


        # clear + draw
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
