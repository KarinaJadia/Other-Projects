def binary_to_decimal(b):
    ''' converts binary to decimal '''
    num = [*b] # splits string into characters
    num.reverse() # reverses it so it's from lowest to highest and i can work with it better

    result = 0
    for i, j in enumerate(num):
        j = int(j) # converts to int so i can use it
        result = result + j*(2**i) # basically takes the number (0 or 1) and multiplies it with 2 to the power of it's position
    return result

# tests for binary to decimal:
# A = [0,1]
# for i in A:
#     for j in A:
#         for k in A:
#             for l in A:
#                 st = str(i)+str(j)+str(k)+str(l)
#                 print(f'{i}{j}{k}{l}: {binary_to_decimal(st)}')

stay = True
while stay:
    where = input('Welcome to this! Are you converting a number to or from decimal system? [to] or [from]: ')

    if where == 'to':
        conversion = input('Excellent! Now are you converting to binary 4 bit or hexadecimal? [b] or [h]: ')
        if conversion == 'b':
            inp = input('input number: ')
            print(f'result: {binary_to_decimal(inp)}')
        elif conversion == 'h':
            inp = input('input number: ')
            pass
        else:
            print("Sorry, I don't know what you're saying.")
            pass

    elif where == 'from':
        conversion = input('Excellent! Now are you converting from binary 4 bit or hexadecimal? [b] or [h]: ')
        if conversion == 'b':
            inp = input('input number: ')
            pass
        elif conversion == 'h':
            inp = input('input number: ')
            pass
        else:
            print("Sorry, I don't know what you're saying.")
            pass

    else:
        print("Sorry, I don't know what you're saying.")

    stay = input('Would you like to try again? [y] or [n]: ')
    if stay == 'y':
        stay = True
    else:
        stay = False