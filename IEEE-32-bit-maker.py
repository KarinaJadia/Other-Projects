''' converts number to IEEE 754 32-bit precision floating point format'''

# the functions that help

def to_binary(b):
    ''' converts decimal to binary '''
    res = [] # stores the result as a list
    b = int(b) # converts input to int

    while b != 0: # loops and does the cute little algorithm i made
        x = b % 2
        b //= 2
        res.append(x)

    res.reverse() # reverses list so the binary is right and converts to string for aesthetic
    result = ''
    for i in res:
        result = result + str(i)

    return result


def dec_to_bi(d):
    ''' converts the decimal part of the input to binary'''
    res = [] # stores result as list

    while d != 1.0: # loops and multiplies for binary decimal conversion
        d *= 2
        res.append(int(d))
        if d > 1:
            d -= 1
    
    result = '' # converts to string for aesthetic
    for i in res:
        result = result + str(i)

    return result


# start of main code

again = True
while again:

    to_convert = input('Number to convert: ')

    if '.' not in to_convert: # catches if user enters an int
        while '.' not in to_convert:
             to_convert = input('Please type a number with a decimal: ')

    if to_convert[-2:] == '.0': # catches if user cheats and enters an int disguised as a double
        while to_convert[-2:] == '.0':
            to_convert = input('Nope, decimal must be a real value: ')

    signed_bit = 0 # first bit
    exponent = 0 # next eight bits
    mantissa = 0 # last 23 bits

    pre_dec = '' # will store the int (easier to do as a string then convert to int)
    post_dec = '' # will store the float (easier to do as a string then convert to float)

    dec = False # this value and loop splits the input into int and float
    for i in to_convert:
        if i == '.':
            dec = True
        if dec:
            post_dec = post_dec + i
        else:
            pre_dec = pre_dec + i

    pre_dec = int(pre_dec)
    post_dec = float(post_dec)

    if pre_dec < 0: # sets up the first bit
        signed_bit = 1
        pre_dec *= -1
        to_convert = to_convert[1:]

    main_bi = to_binary(pre_dec)
    dec_bi = dec_to_bi(post_dec)

    tot = main_bi + '.' + dec_bi # concatenates the whole thing and converts it; tot is the input converted to binary
    total = float(tot) # this will store scientific notation version of tot

    exp = 0 # counts the exponent for the scientific notation representation
    places = len(str(total)) # this is to keep track of how many decimals to show since the loop adds a lot of extra 0s
    while total > 10:
        exp += 1
        total /= 10

    total = str(total)[0:places] # this makes sure it doesn't add extra zeroes after moving the decimal

    exp += 127 # makes it precise
    bi_dec = to_binary(exp) # makes the binary of the exponent

    print(f'\n{to_convert} in binary: {tot}')
    print(f'signed bit (1 bit): {signed_bit}')
    print(f'exponent (8 bits): {bi_dec}')
    mantissa = total[2:] # splits the binary into mantissa
    while len(mantissa) < 23: # adds zero to the rest of the mantissa to make it 23 bits
        mantissa = mantissa + '0'
    print(f'mantissa (23 bits): {mantissa}')
    print(f'all together ({len(str(signed_bit)) + len(bi_dec) + len(mantissa)} bits): {signed_bit} {bi_dec} {mantissa}\n')

    ag = input('To do this again, type [y]: ')
    if ag != 'y':
        again = False