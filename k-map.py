''' creates and simplifies a k-map '''

def to_binary(b):
    ''' converts decimal to binary '''
    res = [] # stores the result as a list
    b = int(b) # converts input to int

    while b != 0: # loops and does the cute little algorithm i made
        x = b % 2
        b //= 2
        res.append(x)

    if len(res) < 4: # adds zero if the binary is less than zero
        while len(res) < 4:
            res.append(0)

    res.reverse() # reverses list so the binary is right and converts to string for aesthetic
    result = ''
    for i in res:
        result = result + str(i)

    return result

def create_dict():
    ''' creates a 16 input dictionary which can store 1s, 0s, and don't-cares '''
    x = ['0','1']
    dict = {}
    for h in x:
        for i in x:
            for j in x:
                for k in x:
                    y = h + i + j + k
                    dict[y] = 'x'
    return dict

def valid_inpt(inp):
    ''' this function helps by testing if an input is a valid 4-bit int '''
    try:
        inp = int(inp)
        if inp >= 0 and inp <= 15:
            return True
        else:
            print('invalid input')
            return False
    except:
        print('invalid input')
        return False


print('this code can only handle 4 bit data, so it cannot handle a number outside the range of 0-15')
values = create_dict() # initializes the values stored
k_map = [['wxyz', '00', '01', '11', '10'], # initializes k-map
         ['00', 'x', 'x', 'x', 'x'],
         ['01', 'x', 'x', 'x', 'x'],
         ['11', 'x', 'x', 'x', 'x'],
         ['10', 'x', 'x', 'x', 'x']]

yesses = input('type all of the 1 inputs, type done when done: ') # takes positive inputs (only between 0-15)
while yesses != 'done':
    if valid_inpt(yesses):
        values[to_binary(yesses)] = 1    
    yesses = input('input: ')

nos = input('type all of the 0 inputs, type done when done: ') # takes negative inputs (only between 0-15)
while nos != 'done':
    if valid_inpt(nos):
        values[to_binary(nos)] = 0
    nos = input('input: ')