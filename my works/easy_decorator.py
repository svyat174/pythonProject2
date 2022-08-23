def log_errors(func):
    def printer(line):
        try:
            func(line)
            print(f'{line} -  Данные введены верно')
        except ValueError as exc:
            print(f'Что-то тут {line} намудрил c {exc}')
        return line
    return printer


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')

lines = [
    'Ярослав bxh@ya.ru 60',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]

for line in lines:
    check_line(line)
