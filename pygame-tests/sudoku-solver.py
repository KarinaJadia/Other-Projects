import pygame
import sys

pygame.init()

# constants
WIDTH, HEIGHT = 800, 600
SQUARE = 50
SPACE = 60

# window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 15)

# input boxes
boxes = []
pos = -20
colors = [(255, 156, 156), (255, 197, 156), (255, 235, 156),
          (187, 255, 156), (156, 255, 210), (156, 245, 255),
          (156, 191, 255), (171, 156, 255), (240, 156, 255)]
for i in range(81):
    if i % 9 == 0:
        pos += SPACE
    box = {
        "x": 80 + i % 9 * SPACE,
        "y": pos,
        "passive color": (76, 153, 186),
        "color": (76, 153, 186),
        "text": '', # the text stored in it
        "active": False,
        "id": i
    }
    boxes.append(box)

# game
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in boxes:
                if pygame.Rect(box['x'], box['y'], SQUARE, SQUARE).collidepoint(event.pos): 
                    box['active'] = True
                    box['color'] = 'lightskyblue3'
                else:
                    box['active'] = False
                    box['color'] = box['passive color']

        # keys
        if event.type == pygame.KEYDOWN:

            # if enter key is clicked
            if event.key == pygame.K_KP_ENTER:
                pygame.draw.circle(screen, "red", (WIDTH-15, HEIGHT-15), 18)

            # if backspace is clicked
            elif event.key == pygame.K_BACKSPACE:
                for box in boxes:
                    if box['active'] == True:
                        box['text'] = box['text'][:-1]

            # else update text
            else:
                for box in boxes:
                    if box['active'] == True:
                        box['text'] += event.unicode  

    # renders text
    text = font.render(f'hit enter to solve puzzle', True, "white", "black")
    textRect = text.get_rect()
    textRect.center = (95, 15)
    screen.blit(text, textRect)
    
    # create boxes
    for box in boxes:
        pygame.draw.rect(screen, box['color'], pygame.Rect(box['x'], box['y'], SQUARE, SQUARE))
        text_surface = font.render(box['text'], True, (255, 255, 255)) 
        # render at position stated in arguments 
        screen.blit(text_surface, (pygame.Rect(box['x'], box['y'], SQUARE, SQUARE).x+20, pygame.Rect(box['x'], box['y'], SQUARE, SQUARE).y+20))

    pygame.display.update()
    clock.tick(60)