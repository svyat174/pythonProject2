import random
number = random.randint(1, 10)
for kk in range(5):
    kk = int(input('enter num: '))
    if kk < number:
        print('less')
    if kk > number:
        print('more')
    if kk == number:
        print('you are win!!!')
        break
else:
    print('you lose!!!')