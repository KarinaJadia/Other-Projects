'''
example inputs/outputs:
P4 + O2 = P2O5 -> 1, 5, 2
MgF2 + Li2CO3 = MgCO3 + LiF -> 1, 1, 1, 2
Al + H2SO4 = Al2(SO4)3 + H3 -> 2, 3, 1, 3
'''

def splitter(eq):
    ''' splits the equation into left and right '''
    d = {'left': [], 'right': []}
    eq = eq.split()

    flag = 'left'
    for i in eq:
        if i == '=':
            flag = 'right'
        elif i == '+':
            pass
        elif flag == 'left':
            d['left'].append(i)
        else:
            d['right'].append(i)

    return d

if __name__ == "__main__":
    inp = input('enter equation: ')
    parsed = splitter(inp)
    print(parsed)