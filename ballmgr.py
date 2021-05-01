# Defines the ball class

import pygame
import random

#ballimage = "small_tennis.png"
ballimage = "deathstar1.png"

class Ball:
    # PyGame class defines the ball and behavior
    def __init__(self, WIDTH, HEIGHT):
        # Load the ball image
        self.image = pygame.image.load(ballimage)
        # Resize the ball image
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.speed = [0, 1]  # Ball velocity
        self.rect = self.image.get_rect()  # Creates the movable sprite
        self.alive = True  # Ball hasn't dropped
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH

    def update(self):
        # Allows for logic while updating sprites
        if self.rect.top < 0:
            # Change direction if we've reached the roof
            self.speed[1] = -self.speed[1]  # Reverse Movement
            self.speed[0] = random.uniform(-4, 4)  # Random X Direction
        elif self.rect.left < 0 or self.rect.right > self.WIDTH:
            # We hit a wall
            self.speed[0] = -self.speed[0]  # Change X Direction
        elif self.rect.bottom > self.HEIGHT:
            # Hit the floor
            self.alive = False  # The ball is dead (dropped)
        self.move()  #Execute the move method

    def move(self):
        # Perform the move
        self.rect = self.rect.move(self.speed)
