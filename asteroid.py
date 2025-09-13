from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        # self.x = x
        # self.y = y
        # self.radius = radius
        super().__init__(x,y,radius)

    def draw(self,screen):
        # pygame.draw.circle(screen,"white",[self.x,self.y],self.radius,2)
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt

    def checkCollision(self,otherShape):
        distance = pygame.math.Vector2.distance_to(self.position,otherShape.position)
        return distance > (self.radius + otherShape.radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        randomAngle = random.uniform(20,50)
        vel1 = self.velocity.rotate(randomAngle)
        vel2 = self.velocity.rotate(-randomAngle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)

        asteroid1.velocity = vel1 * 1.2
        asteroid2.velocity = vel2