import pygame  # Provides PyGame framework
import random  # Used for randomization
from ballmgr import Ball

# Set Constants
WIDTH = 800  # Screen Width
HEIGHT = 600  # Screen Height
BACKGROUND = (0, 0, 0)  # Background Color

def main():
    pygame.init()  # Initialize the PyGame environment
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set screen size
    clock = pygame.time.Clock()  # Create Clock for managing time

    # Create Ball Objects.  Three for your average juggler
    ball1 = Ball(WIDTH, HEIGHT)  # First Ball
    ball2 = Ball(WIDTH, HEIGHT)  # Second Ball
    ball3 = Ball(WIDTH, HEIGHT)  # Third Ball

    balls = [ball1, ball2, ball3]  # List of balls in play
    score = 0  # Initialize the juggler's score
    gameover = False  # Initialize game as running

    while not gameover:
        # Keep looping while game isn't over.
        for event in pygame.event.get():
            # Process any events captured by pygame
            if event.type == pygame.MOUSEBUTTONDOWN:
                # React to mouse click event
                for ball in balls:
                    # Run check on each ball in play
                    if ball.rect.collidepoint(pygame.mouse.get_pos()):
                        # We juggled a ball!
                        ball.speed[0] = random.randrange(-4, 4)  # Random X direction random direction
                        ball.speed[1] = -2 # Fast Y direction
                        score += 1  # Increase Score
                        break
        screen.fill(BACKGROUND)  # Background color fill

        for i, ball in enumerate(balls):
            # Looping through all the balls in play
            if ball.alive:
                # If the ball is alive, update it's location
                screen.blit(ball.image, ball.rect)
                ball.update()
            if not ball.alive:
                # If the ball was dropped, remove it from the list
                del balls[i]
        if len(balls) == 0:
            # We dropped all the balls
            gameover = True  # Game over

        pygame.display.flip()  # Repaints the display w/ new object positions
        clock.tick(60)  # Refresh rate in milliseconds.
    # Print Game Over message and display score
    print(f"Game Over.  You juggled balls {score} times.")

if __name__ == "__main__":
    # This is executed when this script is ran, not imported.
    main()