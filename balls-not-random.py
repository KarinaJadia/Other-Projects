import pygame
import sys
import random

amount = int(input('how many balls: '))

pygame.init()

# important ball variables
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
FPS = 60

# window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

clock = pygame.time.Clock()

# stores the balls
balls = []

# creates the balls as a dictionary
for _ in range(amount):
    ball = {
        "x": WIDTH//amount * _,
        "y": HEIGHT//2,
        "color": [255//amount * _, 0, 255],
        "speed": [0, 1+_*0.25],
        "color_direction": 1,  # allows ball to change colors
    }
    balls.append(ball)

# main game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update ball positions
    for ball in balls:
        ball["color"][1] += ball["color_direction"]
        
        # reverse the direction when it reaches 0 or 255
        if ball["color"][1] == 0 or ball["color"][1] == 255:
            ball["color_direction"] *= -1
        
        ball["y"] += ball["speed"][1]

        # the bounce
        if ball["y"] < BALL_RADIUS or ball["y"] > HEIGHT - BALL_RADIUS:
            ball["speed"][1] *= -1

    # bg
    screen.fill((0, 0, 0))

    # makes the balls
    for ball in balls:
        pygame.draw.circle(screen, ball["color"], (int(ball["x"]), int(ball["y"])), BALL_RADIUS)

    pygame.display.update()
    clock.tick(FPS)