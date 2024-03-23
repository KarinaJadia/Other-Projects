# input the decimal part of the number to generate the mantissa
todo = float(input('input number: '))
final = ''

for i in range(1,24):
    print(f'{i}: {todo} * 2 = {int(todo*2)}')
    todo *= 2
    if todo > 1:
        todo -= 1

    final = final + str(int(todo*2))

print('final mantissa:', final)