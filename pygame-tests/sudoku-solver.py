import pygame
import sys
from sudoku_class import box

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

# input boxes set up
boxes = [] # stores all box objects
s1 = [] # s1-s9 is pointers for each set
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
s8 = []
s9 = []

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
    boxes.append(box(80 + i % 9 * SPACE, pos, colors[(i//9)//3][(i%9)//3], colors[(i//9)//3][(i%9)//3],set_num[(i//9)//3][(i%9)//3]*100 + (i//9+1) * 10 + i%9+1, i))
    if set_num[(i//9)//3][(i%9)//3] == 1:
        s1.append(i)
    elif set_num[(i//9)//3][(i%9)//3] == 2:
        s2.append(i)
    elif set_num[(i//9)//3][(i%9)//3] == 3:
        s3.append(i)
    elif set_num[(i//9)//3][(i%9)//3] == 4:
        s4.append(i)
    elif set_num[(i//9)//3][(i%9)//3] == 5:
        s5.append(i)
    elif set_num[(i//9)//3][(i%9)//3] == 6:
        s6.append(i)
    elif set_num[(i//9)//3][(i%9)//3] == 7:
        s7.append(i)
    elif set_num[(i//9)//3][(i%9)//3] == 8:
        s8.append(i)
    elif set_num[(i//9)//3][(i%9)//3] == 9:
        s9.append(i)

def solve():
    unsolved_pointers = []
    for box in boxes:
        if box.text == '':
            unsolved_pointers.append(box.pointer)
            box.text = str(box.id)
            box.passive_color = (252, 186, 3)
            box.color = (252, 186, 3)
        else:
            box.solved = True
            box.possibles = []
    print(unsolved_pointers)

# game
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            # if a box is clicked
            for box in boxes:
                if pygame.Rect(box.x, box.y, SQUARE, SQUARE).collidepoint(event.pos): 
                    box.active = True
                    box.color = (36, 36, 36)
                else:
                    box.active = False
                    box.color = box.passive_color

        # keys
        if event.type == pygame.KEYDOWN:

            # if enter key is clicked
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                solve()

            # if tab key is clicked, move to next box
            elif event.key == pygame.K_TAB:
                for box in boxes:
                    if box.active == True:
                        pointer = box.pointer + 1
                        box.active = False
                        boxes[pointer].active = True
                        boxes[pointer].color = (36, 36, 36)
                        box.color = box.passive_color
                        break
    
            # if backspace is clicked
            elif event.key == pygame.K_BACKSPACE:
                for box in boxes:
                    if box.active == True:
                        box.text = box.text[:-1]

            # else update text
            else:
                for box in boxes:
                    if box.active == True:
                        box.text += event.unicode
    # resets screen
    screen.fill((0, 0, 0))

    # renders text
    text = font.render(f'hit enter to solve puzzle', True, "white", "black")
    textRect = text.get_rect()
    textRect.center = (95, 15)
    screen.blit(text, textRect)
    
    # create boxes
    for box in boxes:
        pygame.draw.rect(screen, box.color, pygame.Rect(box.x, box.y, SQUARE, SQUARE))
        text_surface = font.render(box.text, True, (255, 255, 255)) 
        # render at position stated in arguments 
        screen.blit(text_surface, (pygame.Rect(box.x, box.y, SQUARE, SQUARE).x+20, pygame.Rect(box.x, box.y, SQUARE, SQUARE).y+20))

    pygame.display.update()
    clock.tick(60)