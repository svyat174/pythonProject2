zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

zoo.insert(1, 'bear')
print(zoo)

birds = ['rooster', 'ostrich', 'lark']

zoo.extend(birds)
print(zoo)


del zoo[3]
print(zoo)


print(zoo.index('lion') + 1)
print(zoo.index('lark') + 1)