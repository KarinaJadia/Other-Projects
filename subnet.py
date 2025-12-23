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

def sub_to_list(a):
    ''' takes a subnet of format a.b.c.d/e and returns a list '''
    b = a.split('.')
    c = b[-1].split('/')
    b.append(c[0])
    b.append(c[1])
    b.remove(b[-3])

    return b

def list_to_sub(b):
    ''' takes a list and returns string in format a.b.c.d/e '''
    return b[0] + '.' + b[1] + '.' + b[2] + '.' + b[3] + '/' + b[4]

if __name__ == "__main__":
    # r = input('input subnet: ') # 68.168.0.34/29
    r = '68.168.0.34/29'

    b = sub_to_list(r)

    host_bits = 32 - int(b[-1])
    
    for i in range(len(b)):
        b[i] = to_binary(int(b[i]))
    
    address = list_to_sub(b) # address in bin form
    netmask = f'255.255.255.255'.split('.')
    
    # netmask is all ones except n zeros where n is number of host bits
    for i in range(len(netmask)):
        netmask[i] = to_binary(int(netmask[i]))

    netmask[-1] = netmask[-1] = '1' * (8 - host_bits) + '0' * host_bits
    netmask = netmask[0] + '.' + netmask[1] + '.' + netmask[2] + '.' + netmask[3]

    print(f'original address: {r}')
    print(f'binary address: {address}')
    print(f'netmask: {netmask}')
    print(f'hosts: {2**host_bits - 2}')