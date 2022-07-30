import random
number = random.randint(1, 10)
for k in range(3):
    k = int(input('enter num: '))
    if k < number:
        print('you num is less number')
    if k > number:
        print('you num is more number')
    if k == number:
        print('you are win!!!')
        break
else:
    print('you lose!!!')