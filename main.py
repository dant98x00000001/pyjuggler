import pygame  # Provides PyGame framework
import random  # Used for randomization
from ballmgr import Ball

# Set Constants
WIDTH = 800  # Screen Width
HEIGHT = 600  # Screen Height
WINDOW_SIZE = (WIDTH, HEIGHT)  # Window Size tuple
BACKGROUND_COLOR = (0, 255, 0)  # Background Color
# DIFFICULTY = 3  # Number of Balls to juggle


def main():
    pygame.init()  # Initialize the PyGame environment
    screen = pygame.display.set_mode(WINDOW_SIZE)  # Set screen size
    clock = pygame.time.Clock()  # Create Clock for managing time
    background_image = pygame.transform.scale(pygame.image.load("galaxy_background.jpg"), WINDOW_SIZE)
    
    DIFFICULTY = int(input('How many death stars do you want to play with... tough guy?\n'))

    # Create Ball Objects.  Three for your average juggler
    balls = []  # Initialize List of balls in play
    for i in range(DIFFICULTY):
        # Dynamically add the balls per difficulty rating
        balls.append(Ball(WIDTH, HEIGHT))

    score = 0  # Initialize the juggler's score
    gameover = False  # Initialize game as running

    while not gameover:
        if pygame.mouse.get_focused():
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

            #screen.fill(BACKGROUND)  # Background color fill
            screen.blit(background_image, [0, 0])  # Sets the background to an image.

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
        else:
            # Get events occuring while the window is not in focus
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # If there is a QUIT event (user clicked close)
                    balls = []  # Remove all the remaining balls
            pygame.event.wait(5)  # Give a little bit of wait time before checking again
        pygame.display.flip()  # Repaints the display w/ new object positions
        clock.tick(60)  # Refresh rate in milliseconds.

    # Print Game Over message and display score
    print(f"Game Over.  You juggled balls {score} times.")

if __name__ == "__main__":
    # This is executed when this script is ran, not imported.
    main()