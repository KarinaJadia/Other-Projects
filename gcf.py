print('enter 0 to quit')
ints = input('enter numbers, separated by a space (only works for integers): ')
while not ints == '0':
    ints = ints.split() # splits it
    ints = [int((int(i)**2)**(1/2)) for i in ints] # converts them to absolute value ints

    factors = [i for i in range(2, max(ints)+1)] # assume all numbers from 2-max are factors

    counter = 1
    while counter <= max(ints): # goes through list, if a number is not divisible by list, remove it
        for i in ints:
            if not i % counter == 0:
                factors.remove(counter)
                break
        counter += 1
    
    if len(factors) > 0:
        print('factors:',end=' ')
        for i in factors:
            print(i, end=' ')
    else:
        print('no common factors', end='')

    ints = input('\nenter numbers, separated by a space (only works for integers): ')