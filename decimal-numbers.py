def from_binary(b):
    ''' converts binary to decimal '''
    num = [*b] # splits string into characters
    num.reverse() # reverses it so it's from lowest to highest and i can work with it better

    result = 0 # stores the final result

    for i, j in enumerate(num): # the cute little algorithm i made
        j = int(j) # converts to int so i can use it
        result = result + j*(2**i) # basically takes the number (0 or 1) and multiplies it with 2 to the power of it's position
    
    return result


def to_binary(b):
    ''' converts decimal to binary '''
    res = [] # stores the result as a list
    b = int(b) # converts input to int

    for i in range(4): # loops 4 times and does the cute little algorithm i made
        x = b % 2
        b //= 2
        res.append(x)

    res.reverse() # reverses list so the binary is right and converts to string for aesthetic
    result = ''
    for i in res:
        result = result + str(i)

    return result


def to_hex(h):
    ''' converts decimal to hexadecimal '''
    res = []
    h = int(h)


stay = True
while stay:
    where = input('Welcome to this! Are you converting a number to or from 4 bit/hexadecimal? [to] or [from]: ')

    if where == 'to':
        conversion = input('Excellent! Now are you converting to binary 4 bit or hexadecimal? [b] or [h]: ')
        if conversion == 'b':
            inp = input('input number (between 0-15): ')
            print(f'result: {to_binary(inp)}')
        elif conversion == 'h':
            inp = input('input number: ')
            print(f'result: {to_hex(inp)}')
        else:
            print("Sorry, I don't know what you're saying.")

    elif where == 'from':
        conversion = input('Excellent! Now are you converting from binary 4 bit or hexadecimal? [b] or [h]: ')
        if conversion == 'b':
            inp = input('input number: ')
            print(f'result: {from_binary(inp)}')
        elif conversion == 'h':
            inp = input('input number: ')
        else:
            print("Sorry, I don't know what you're saying.")

    else:
        print("Sorry, I don't know what you're saying.")

    stay = input('Would you like to try again? [y] or [n]: ')
    if stay == 'y':
        stay = True
    else:
        stay = False