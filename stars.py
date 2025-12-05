import random

stars = [' · ',' * ',' ⋆ ',' ⊹ ',' ˚ ',' ✹ ',' ✦ ',' ✵ ']
print()
for x in range(10):
    for i in range(12):
        star = random.randint(0,35)
        if star < 8:
            print(stars[star], end='')
        else:
            print('  ',end='')
    print()
print()