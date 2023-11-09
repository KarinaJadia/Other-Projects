import pygame
import sys
import random

# important ball variables
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
FPS = 60
BLINK_TIME = 50 # how long the ball blinks for when hit
MAX_HITS = 100

print('\nwelcome to dodgeball! use the arrow keys or WASD to avoid the balls')
print(f'the more balls you hit, the larger you get. if you get hit {MAX_HITS} times, game over!')
amount = int(input('\nhow many balls: '))

pygame.init()

# window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

clock = pygame.time.Clock()

# stores the balls
balls = []

# player position and trail
user_ball = {"x": WIDTH/2, "y": HEIGHT/2, "hits":0, "radius": 10}
trail = [(WIDTH/2, HEIGHT/2) for i in range(15)]
trail_radius = [10 for i in range(15)]

# updates the trail by adding the newest element to the beginning (this is a walmart queue)
def update_trail(x, lis):
    lis.insert(0, x)
    lis.pop(len(lis)-1)
    return lis

# creates the balls as a dictionary
for _ in range(amount):
    ball = {
        "x": random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS),
        "y": random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS),
        "color": (random.randint(0, 255), 0, 255),
        "speed": [random.randint(1,5), random.randint(1,5)],
        "hit": 0 # basically tracks if the ball's been hit like a timer so that it can blink
    }
    balls.append(ball)

font = pygame.font.Font('freesansbold.ttf', 25)

# main game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if user_ball["radius"] == MAX_HITS:
        print('\ngame over!\n')
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
        ball = balls[i]

        # for changing the ball colors
        if ball["hit"] > 0:
            ball["hit"] = ball["hit"] + 1
        if ball["hit"] == BLINK_TIME:
            ball["hit"] = 0

        # handles collisions with user's ball
        dis = ((ball["x"] - user_ball["x"]) ** 2 + (ball["y"] - user_ball["y"]) ** 2) ** 0.5
        if dis < user_ball["radius"] or dis < 30:
            user_ball["hits"] += 1
            user_ball["radius"] += 1

            ball["x"] = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
            ball["y"] = random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS)
            ball["hit"] = ball["hit"] + 1

        # handles collisions between dodgeballs
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
    textRect.center = (50, 20)
    screen.blit(text, textRect)

    # makes the trail
    trail = update_trail((user_ball["x"], user_ball["y"]), trail)
    trail_radius = update_trail(user_ball["radius"], trail_radius)
    for i in range(len(trail)):
        pygame.draw.circle(screen, (150-i*10, 150-i*10, 150-i*10), (trail[i]), trail_radius[i])

    # user's ball
    pygame.draw.circle(screen, "red", (user_ball["x"], user_ball["y"]), user_ball["radius"])

    blink = ['1','2','3','4','5','6']
    # makes the dodgeballs
    for ball in balls:
        if str(ball["hit"])[-1] in blink:
            pygame.draw.circle(screen, "red", (int(ball["x"]), int(ball["y"])), BALL_RADIUS)
        elif ball["hit"] > 0:
            pygame.draw.circle(screen, "black", (int(ball["x"]), int(ball["y"])), BALL_RADIUS)
        else:
            pygame.draw.circle(screen, ball["color"], (int(ball["x"]), int(ball["y"])), BALL_RADIUS)

    pygame.display.update()
    clock.tick(FPS)