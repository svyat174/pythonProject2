ops = {
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '//': lambda x, y: x // y,
    '%': lambda x, y: x % y,

}


def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation in ops:
        func = ops[operation]
        value = func(operand_1, operand_2)
    else:
        raise ValueError(f'Unknow operation {operation}')
    return value


def get_lines(file_name):
    with open(file_name, 'r') as ff:
        for line in ff:
            line = line[:-1]
            yield line


total = 0
for line in get_lines(file_name='calc.txt'):
    try:
        total += calc(line)
        print(f' {line} = ', round(calc(line), 2))
    except ValueError as exp:
        if 'unpack' in exp.args[0]:
            print(f'Не хватает операндов {exp} в строке {line}')
        else:
            print(f'Не могу преобразовать к целому числу {exp} в строке {line}')

print(f'Total: {round(total, 2)}')
