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

    while b != 0: # loops and does the cute little algorithm
        x = b % 2
        b //= 2
        res.append(x)

    res.reverse() # reverses list so the binary is right and converts to string for aesthetic
    result = ''
    for i in res:
        result = result + str(i)

    return result


print('how to use - type tb [number] to convert number to binary or td [number] to convert number to decimal')
stri = input('input: ').split()
while stri[0] != '0':
    
    if stri[0] == 'tb':
        print(f'result: {to_binary(int(stri[1]))}')
    elif stri[0] == 'td':
        print(f'result: {from_binary(stri[1])}')

    else:
        print("Sorry, I don't know what you're saying.")

    stri = input('enter 0 to quit or enter input to calculate next number: ').split()