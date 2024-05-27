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
        "id": set_num[(i//9)//3][(i%9)//3]*100 + (i//9+1) * 10 + i%9+1 # i think it will make it easier to reference
        # i//9+1 is row (1-9) and i%9+1 is column (1-9)
    }
    boxes.append(box)

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
        if box['text'] == '':
            box['passive color'] = (252, 186, 3)
            box['color'] = (252, 186, 3)

        # each set dictionary will store the leftover possible solutions within the set and the unsolved boxes
        if box['id'] < 200:
            if box['text'] != '':
                set1[box['id']] = int(box['text'])
                set1['possible'].remove(int(box['text']))
            else:
                set1['unsolved'].append(box['id'])
        elif box['id'] < 300:
            if box['text'] != '':
                set2[box['id']] = int(box['text'])
                set2['possible'].remove(int(box['text']))
            else:
                set2['unsolved'].append(box['id'])
        elif box['id'] < 400:
            if box['text'] != '':
                set3[box['id']] = int(box['text'])
                set3['possible'].remove(int(box['text']))
            else:
                set3['unsolved'].append(box['id'])
        elif box['id'] < 500:
            if box['text'] != '':
                set4[box['id']] = int(box['text'])
                set4['possible'].remove(int(box['text']))
            else:
                set4['unsolved'].append(box['id'])
        elif box['id'] < 600:
            if box['text'] != '':
                set5[box['id']] = int(box['text'])
                set5['possible'].remove(int(box['text']))
            else:
                set5['unsolved'].append(box['id'])
        elif box['id'] < 700:
            if box['text'] != '':
                set6[box['id']] = int(box['text'])
                set6['possible'].remove(int(box['text']))
            else:
                set6['unsolved'].append(box['id'])
        elif box['id'] < 800:
            if box['text'] != '':
                set7[box['id']] = int(box['text'])
                set7['possible'].remove(int(box['text']))
            else:
                set7['unsolved'].append(box['id'])
        elif box['id'] < 900:
            if box['text'] != '':
                set8[box['id']] = int(box['text'])
                set8['possible'].remove(int(box['text']))
            else:
                set8['unsolved'].append(box['id'])
        else:
            if box['text'] != '':
                set9[box['id']] = int(box['text'])
                set9['possible'].remove(int(box['text']))
            else:
                set9['unsolved'].append(box['id'])
    print(set1)

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