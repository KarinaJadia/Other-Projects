'''
example inputs/outputs:
P4 + O2 = P2O5 -> 1, 5, 2
MgF2 + Li2CO3 = MgCO3 + LiF -> 1, 1, 1, 2
Al + H2SO4 = Al2(SO4)3 + H3 -> 2, 3, 1, 3
'''

def lr_splitter(eq):
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

def atom_splitter(eq):
    ''' splits the equation by molecule '''
    d = {}
    for i in range(len(eq)):
        if eq[i].isalpha():
            if eq[i].islower():
                continue
            elif i+1 < len(eq) and eq[i+1].islower():
                d[eq[i] + eq[i+1]] = 0
            else:
                d[eq[i]] = 0

    return d

if __name__ == "__main__":
    # inp = input('enter equation: ')
    inp = 'MgF2 + Li2CO3 = MgCO3 + LiF'
    parsed = lr_splitter(inp)
    print(parsed)

    moleculized = atom_splitter(inp)
    print(moleculized)