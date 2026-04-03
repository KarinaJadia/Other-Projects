''' takes a four digit number and does kaprekar's routine, all four digit numbers add up to 6174 eventually'''

def subtractor(l, num):
    l.append(num)
    big = int(''.join(sorted(str(num), reverse=True)))
    small = int(''.join(sorted(str(num))))
    new = big - small
    return l, new

num = int(input('four digit number: '))
l = []
c = 0

if len(set(str(num))) == 1:
    print('all digits cannot be the same!')
    exit()

while not num == 6174 and not c == 1000:
    l, num = subtractor(l, num)
    c += 1

if num == 6174:
    l.append(num)
    print(f'number of loops required: {len(l)-1}')
    print('path:', l)
else:
    print('did not achieve 6174')
    # print('path:', l)