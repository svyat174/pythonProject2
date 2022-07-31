# (цикл while)
a, b = int(input('Enter integer num_1:')), int(input('Enter integer num_2:'))
if a < b:
    print('ERR')
else:
    next_a = a
    while next_a > b:
        next_a -= b
        if next_a < b:
            print('Целочисленное деление', a, 'на', b, 'остаток', next_a, 'Результат:', int((a - next_a) / b))
        elif next_a == b:
            print('Остаток 0! Результат деления:', int(a / b))
