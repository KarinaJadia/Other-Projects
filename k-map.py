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


x = ['0','1']
map = {} # the values of the k-map, which will stores 0s and 1s and xs
for h in x:
    for i in x:
        for j in x:
            for k in x:
                y = h + i + j + k
                map[y] = 'x'
