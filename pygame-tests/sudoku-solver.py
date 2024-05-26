import pygame
import sys

pygame.init()

# constants
WIDTH, HEIGHT = 800, 600 # size of window
SQUARE = 50 # size of boxes
SPACE = 60 # space between boxes

# window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 15)

# input boxes
boxes = []
pos = -20
colors = [[(105, 64, 70), (105, 80, 64), (105, 93, 64)], # stores the colors of the box
          [(64, 105, 89), (64, 102, 105), (64, 81, 105)],
          [(64, 64, 105), (87, 64, 105), (98, 64, 105)]]
set_num = [[1, 2, 3], # to make life easier
          [4, 5, 6],
          [7, 8, 9]]

for i in range(81):
    if i % 9 == 0:
        pos += SPACE
    box = {
        "x": 80 + i % 9 * SPACE,
        "y": pos,
        "passive color": colors[(i//9)//3][(i%9)//3], # this is the permanent color
        "color": colors[(i//9)//3][(i%9)//3], # this is so that it can have a 'clicked on' color
        "text": '', # the text stored in it
        "active": False,
        "row": i // 9 + 1, # stores row (goes from 1 to 9)
        "col": i % 9 + 1, # stores column (goes from 1 to 9)
        "set": set_num[(i//9)//3][(i%9)//3] # which 'set' of boxes it is (goes from 1 to 9)
    }
    boxes.append(box)

def solve():
    for box in boxes:
        if box['text'] == '':
            box['passive color'] = 'red'
            box['color'] = 'red'

# game
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            # if a box is clicked
            for box in boxes:
                if pygame.Rect(box['x'], box['y'], SQUARE, SQUARE).collidepoint(event.pos): 
                    box['active'] = True
                    box['color'] = (36, 36, 36)
                else:
                    box['active'] = False
                    box['color'] = box['passive color']

        # keys
        if event.type == pygame.KEYDOWN:

            # if enter key is clicked
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                solve()

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