def to_binary(b):
    ''' converts decimal to binary '''
    res = [] # stores the result as a list

    while b != 0: # loops and does the binarying
        x = b % 2
        b //= 2
        res.append(x)

    res.reverse() # reverses list so the binary is right and converts to string for aesthetic
    result = ''
    for i in res:
        result = result + str(i)

    while len(result) != 8:
        result = '0' + result

    return result

if __name__ == "__main__":
    # raw = input('input subnet: ') # 68.168.0.34/29
    raw = '68.168.0.34/29'

    # converting to array for ease of calculation
    raw = raw.split('.')
    c = raw[-1].split('/')
    raw.append(c[0])
    raw.append(c[1])
    raw.remove(raw[-3])
    
    for i in range(len(raw)):
        raw[i] = to_binary(int(raw[i]))
    
    print(raw)