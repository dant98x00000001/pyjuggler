import pygame  # Provides PyGame framework
import random  # Used for randomization
from ballmgr import Ball
from time import sleep

import os, sys
APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))

# Set Constants
WIDTH = 800  # Screen Width
HEIGHT = 600  # Screen Height
WINDOW_SIZE = (WIDTH, HEIGHT)  # Window Size tuple
BACKGROUND_COLOR = (0, 255, 0)  # Background Color
DIFFICULTY = 3  # Number of Balls to juggle

def getsounds():
    """generate list of sounds"""
    blaster_sounds = list()
    blaster_folder = os.path.join(APP_FOLDER, "blaster_sounds")
    for file in [os.path.join(blaster_folder, f) for f in os.listdir(blaster_folder)]:
        print(file)
        blaster_sounds.append(pygame.mixer.Sound(file))
    fail_sounds = list()
    fail_folder = os.path.join(APP_FOLDER, "fail_sounds")
    for file in [os.path.join(fail_folder, f) for f in os.listdir(fail_folder)]:
        print(file)
        fail_sounds.append(pygame.mixer.Sound(file))
    gameover = pygame.mixer.Sound("imperial_march_rock.mp3")
    return blaster_sounds, fail_sounds, gameover


def main():
    pygame.init()  # Initialize the PyGame environment
    screen = pygame.display.set_mode(WINDOW_SIZE)  # Set screen size
    clock = pygame.time.Clock()  # Create Clock for managing time
    background_image = pygame.transform.scale(pygame.image.load("galaxy_background.jpg"), WINDOW_SIZE)
    gameover_image = pygame.transform.scale(pygame.image.load("game-over-death.jpg"), WINDOW_SIZE)
    # Sounds
    blaster_sounds, fail_sounds, gameover_sound = getsounds()

    # Create Ball Objects.  Three for your average juggler
    balls = []  # Initialize List of balls in play
    for i in range(DIFFICULTY):
        # Dynamically add the balls per difficulty rating
        balls.append(Ball(WIDTH, HEIGHT))

    score = 0  # Initialize the juggler's score
    prevscore = 0
    gameover = False  # Initialize game as running
    pygame.display.set_caption(f'PyJuggling Score: {score}')
    QUIT = False
    while not gameover:
        if score != prevscore:
            pygame.display.set_caption(f'PyJuggling Score: {score}')
        if pygame.mouse.get_focused():
            # Keep looping while game isn't over.
            for event in pygame.event.get():
                # Process any events captured by pygame
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # React to mouse click event
                    pygame.mixer.Sound.play(random.choice(blaster_sounds))
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
                    pygame.mixer.Sound.play(random.choice(fail_sounds))
                    del balls[i]

            if len(balls) <= 1:
                # We dropped all but one ball, which is too easy to juggle.
                # Or we quit the game (zero balls)
                screen.blit(gameover_image, [0, 0])
                pygame.display.update()
                pygame.mixer.Sound.play(gameover_sound)
                QUIT = False
                while pygame.mixer.get_busy() and not QUIT:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            QUIT = True
                    pass
                gameover = True  # Game over

            if score != prevscore and score % 10 == 0:
                prevscore = score
                balls.append(Ball(WIDTH, HEIGHT))
        else:
            # Get events occuring while the window is not in focus
            for event in pygame.event.get():
                if event.type == pygame.QUIT or QUIT:
                    # If there is a QUIT event (user clicked close)
                    balls = []  # Remove all but one the remaining balls

            pygame.event.wait(5)  # Give a little bit of wait time before checking again
        pygame.display.flip()  # Repaints the display w/ new object positions
        clock.tick(60)  # Refresh rate in milliseconds.

    # Print Game Over message and display score
    print(f"Game Over.  You juggled balls {score} times.")
    pygame.quit()

if __name__ == "__main__":
    # This is executed when this script is ran, not imported.
    main()