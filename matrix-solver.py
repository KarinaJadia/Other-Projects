r = -1
c = -1
print('this code will solve an augmented matrix to reduced echelon form')
print("also i do not have any try/catch statements so if you don't follow the input rules, it won't work!")

def print_matrix(m): # makes printing the matrix prettier
    for r in range(len(m)):
        for c in range(len(m[0])):
            print(f'{m[r][c]:.1f}', end=' ')
        print('')
    print('')

def list_yank(m, c): # creates a list of all elements in column c
    lis = []
    for i in range(len(m)):
        lis.append(m[i][c])
    return lis

# takes rows and columns
r_c = input('enter rows and columns as ints separated by a space (example: 3 4): ').split()
r_c = [int(i) for i in r_c]
r, c = r_c[0], r_c[1]

# augmented matrix initialized
m = [['*']*c]*r

# populates augmented matrix
for i in range(r):
    line = input(f'enter {c} numbers for row {i+1} separated by spaces: ').split()
    if len(line) != c:
        while len(line) != c:
            line = input(f'please enter {c} numbers: ').split()
    m[i] = [int(x) for x in line]

print('\nyour augmented matrix:')
print_matrix(m)

to_do = 0 # this keeps track of which column to go to
level = 0 # this keeps track of which row we're on for pivots

while to_do < c and level < r:
    pivot = m[level][to_do] # this is the pivot
    if pivot == 0:
        while pivot == 0:
            level += 1
            pivot = m[level][to_do] # this is the pivot
    col = list_yank(m, to_do) # yanks the column of the pivot
    for i, e in enumerate(col):
        if i == level: # don't touch the pivot level
            pass
        else: # math
            # print('pivot ', pivot)
            multiple = -e/pivot # value to multiply pivot row by to get 0
            # print('multiple ',multiple)
            x = m[i] # row being multiplied
            # print('row to convert ',x)
            m[i] = [m[level][z] * multiple + x[z] for z in range(c)]
            # print(f'final row done: {m[i]}\n')
    # print('')
    # print_matrix(m)
    to_do += 1
    level += 1
    
next = 0
for i in range(len(m)):
    x = m[i]
    for j in x:
        if j != 0 and next == 0:
            next = 1
            z = [x[k]/j for k in range(len(m[0]))]
            m[i] = z
    next = 0

print('completed matrix:')
print_matrix(m)