def calc(line):
    # print(f'read line {line}', flush=True, end='')
    operand_1, opertion, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if opertion == '+':
        value = operand_1 + operand_2
    elif opertion == '-':
        value = operand_1 - operand_2
    elif opertion == '*':
        value = operand_1 * operand_2
    elif opertion == '/':
        value = operand_1 / operand_2
    elif opertion == '//':
        value = operand_1 // operand_2
    elif opertion == '%':
        value = operand_1 % operand_2
    return value


total = 0
with open('calc.txt', 'r') as ff:
    for line in ff:
        try:
            total += calc(line)
        except ValueError as exp:
            if 'unpack' in exp.args[0]:
                print(f'Не хватает операндов {exp} в строке {line}', end='')
            else:
                print(f'Не могу преобразовать к целому {exp} в строке {line}', end='')
print(f'Total {total}')
