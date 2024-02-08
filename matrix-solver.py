r = -1
c = -1
print('this code will solve an augmented matrix to reduced echelon form!')


def not_proper_size(x, a, b):
    # this will be used to make sure values are proper
    if x < a or x > b:
        print(f'please enter a number between {a} and {b}')
    return x < a or x > b

def print_matrix(m):
    for r in range(len(m)):
        for c in range(len(m[0])):
            print(f'{m[r][c]}', end=' ')
        print('\n')


while not_proper_size(r, 0, 5): # makes sure that the inputs are proper type and size
    try:
        r = int(input('rows (between 1 and 5): '))
    except:
        valueError: print('please enter an integer')

while not_proper_size(c, 0, 5): # makes sure that the inputs are proper type and size
    try:
        c = int(input('columns (between 1 and 5): '))
    except:
        valueError: print('please enter an integer')

m = [['*']*c]*r

print_matrix(m)