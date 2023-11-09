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

# player position
user_ball = {"x": WIDTH/2, "y": HEIGHT/2, "hits":0}

# creates the balls as a dictionary
for _ in range(amount):
    ball = {
        "x": random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS),
        "y": random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS),
        "color": (random.randint(0, 255), 0, 255),
        "speed": [random.randint(1,5), random.randint(1,5)],
    }
    balls.append(ball)

font = pygame.font.Font('freesansbold.ttf', 25)

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

        # handles collisions with user's ball
        ball = balls[i]
        dis = ((ball["x"] - user_ball["x"]) ** 2 + (ball["y"] - user_ball["y"]) ** 2) ** 0.5
        if dis < 35:
            user_ball["hits"] += 1

            # trying to make the collisions realistic
            if ball["x"] + user_ball["x"] > 0.5 * (ball["y"] + user_ball["y"]):
                ball["speed"][0] = ball["speed"][0] * -1
            elif ball["y"] + user_ball["y"] > 0.5 * (ball["x"] + user_ball["x"]):
                ball["speed"][1] = ball["speed"][1] * -1
            else:
                ball["speed"][0] = ball["speed"][0] * -1
                ball["speed"][1] = ball["speed"][1] * -1

        for j in range(i + 1, len(balls)):
            ball1, ball2 = balls[i], balls[j]
            distance = ((ball1["x"] - ball2["x"]) ** 2 + (ball1["y"] - ball2["y"]) ** 2) ** 0.5
            if distance < 2 * BALL_RADIUS:
                # reverses speed of both balls for collision                
                ball1["speed"][0], ball2["speed"][0] = ball2["speed"][0], ball1["speed"][0]
                ball1["speed"][1], ball2["speed"][1] = ball2["speed"][1], ball1["speed"][1]

    # user balls to control
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and not(user_ball["y"] < 10):
        user_ball["y"] -= 10
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and not(user_ball["y"] > HEIGHT-10):
        user_ball["y"] += 10
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and not(user_ball["x"] < 10):
        user_ball["x"] -= 10
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and not(user_ball["x"] > WIDTH-10):
        user_ball["x"] += 10

    # bg
    screen.fill((0, 0, 0))

    # score text
    text = font.render(f'Hits: {user_ball["hits"]}', True, "green", "black")
    textRect = text.get_rect()
    textRect.center = (45, 20)
    screen.blit(text, textRect)

    # user's ball
    pygame.draw.circle(screen, "red", (user_ball["x"], user_ball["y"]), 10)

    # makes the balls
    for ball in balls:
        pygame.draw.circle(screen, ball["color"], (int(ball["x"]), int(ball["y"])), BALL_RADIUS)

    pygame.display.update()
    clock.tick(FPS)