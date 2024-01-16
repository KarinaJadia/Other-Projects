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
        "x": random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS),
        "y": random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS),
        "color": (random.randint(0, 255), 0, 255),
        "speed": [random.randint(1, 11), random.randint(1,11)],
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
        ball["x"] += ball["speed"][0]
        ball["y"] += ball["speed"][1]

        # the bounce
        if ball["x"] < BALL_RADIUS or ball["x"] > WIDTH - BALL_RADIUS:
            ball["speed"][0] *= -1
        if ball["y"] < BALL_RADIUS or ball["y"] > HEIGHT - BALL_RADIUS:
            ball["speed"][1] *= -1

    # collisions
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            ball1, ball2 = balls[i], balls[j]
            # pythagorean theorem go brrr
            distance = ((ball1["x"] - ball2["x"]) ** 2 + (ball1["y"] - ball2["y"]) ** 2) ** 0.5
            if distance < 2 * BALL_RADIUS:
                # reverses speed of both balls for collision                
                ball1["speed"][0], ball2["speed"][0] = ball2["speed"][0], ball1["speed"][0]
                ball1["speed"][1], ball2["speed"][1] = ball2["speed"][1], ball1["speed"][1]

    # bg
    screen.fill((0, 0, 0))

    # makes the balls
    for ball in balls:
        pygame.draw.circle(screen, ball["color"], (int(ball["x"]), int(ball["y"])), BALL_RADIUS)

    pygame.display.update()
    clock.tick(FPS)