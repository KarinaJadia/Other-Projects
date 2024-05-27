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
    boxes.append(box(80 + i % 9 * SPACE, pos, colors[(i//9)//3][(i%9)//3], colors[(i//9)//3][(i%9)//3],set_num[(i//9)//3][(i%9)//3]*100 + (i//9+1) * 10 + i%9+1, i))

def solve():

    set1 = {'possible': [1,2,3,4,5,6,7,8,9],'unsolved': []}
    set2 = {'possible': [1,2,3,4,5,6,7,8,9],'unsolved': []}
    set3 = {'possible': [1,2,3,4,5,6,7,8,9],'unsolved': []}
    set4 = {'possible': [1,2,3,4,5,6,7,8,9],'unsolved': []}
    set5 = {'possible': [1,2,3,4,5,6,7,8,9],'unsolved': []}
    set6 = {'possible': [1,2,3,4,5,6,7,8,9],'unsolved': []}
    set7 = {'possible': [1,2,3,4,5,6,7,8,9],'unsolved': []}
    set8 = {'possible': [1,2,3,4,5,6,7,8,9],'unsolved': []}
    set9 = {'possible': [1,2,3,4,5,6,7,8,9],'unsolved': []}

    for box in boxes:
        # fancy color changing
        if box[box['id']] == '':
            box['passive color'] = (252, 186, 3)
            box['color'] = (252, 186, 3)

        # each set dictionary will store the leftover possible solutions within the set and the unsolved boxes
        if box['id'] < 200:
            if box[box['id']] != '':
                set1['possible'].remove(int(box[box['id']]))
            else:
                set1['unsolved'].append(box['id'])
                set1[box['pos']] = 0
        elif box['id'] < 300:
            if box[box['id']] != '':
                set2[box['id']] = int(box[box['id']])
                set2['possible'].remove(int(box[box['id']]))
            else:
                set2['unsolved'].append(box['id'])
        elif box['id'] < 400:
            if box[box['id']] != '':
                set3[box['id']] = int(box[box['id']])
                set3['possible'].remove(int(box[box['id']]))
            else:
                set3['unsolved'].append(box['id'])
        elif box['id'] < 500:
            if box[box['id']] != '':
                set4[box['id']] = int(box[box['id']])
                set4['possible'].remove(int(box[box['id']]))
            else:
                set4['unsolved'].append(box['id'])
        elif box['id'] < 600:
            if box[box['id']] != '':
                set5[box['id']] = int(box[box['id']])
                set5['possible'].remove(int(box[box['id']]))
            else:
                set5['unsolved'].append(box['id'])
        elif box['id'] < 700:
            if box[box['id']] != '':
                set6[box['id']] = int(box[box['id']])
                set6['possible'].remove(int(box[box['id']]))
            else:
                set6['unsolved'].append(box['id'])
        elif box['id'] < 800:
            if box[box['id']] != '':
                set7[box['id']] = int(box[box['id']])
                set7['possible'].remove(int(box[box['id']]))
            else:
                set7['unsolved'].append(box['id'])
        elif box['id'] < 900:
            if box[box['id']] != '':
                set8[box['id']] = int(box[box['id']])
                set8['possible'].remove(int(box[box['id']]))
            else:
                set8['unsolved'].append(box['id'])
        else:
            if box[box['id']] != '':
                set9[box['id']] = int(box[box['id']])
                set9['possible'].remove(int(box[box['id']]))
            else:
                set9['unsolved'].append(box['id'])

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
                #solve()
                print(boxes[0].x)
    
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