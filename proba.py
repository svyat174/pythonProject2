import random
number = random.randint(1, 10)
for kk in range(3):
    kk = int(input('enter num: '))
    if kk < number:
        print('you num is less number')
    if kk > number:
        print('you num is more number')
    if kk == number:
        print('you are win!!!')
        break
else:
    print('you lose!!!')