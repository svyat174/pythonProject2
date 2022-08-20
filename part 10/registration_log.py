class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class NotAgeError(Exception):
    pass


list_ok = []
list_nok = []


with open('registrations.txt', 'r', encoding='utf-8') as file:
    for line in file:
        try:
            name, e_mail, age = line.split(' ')
            age = int(age)
            if name.isalpha():
                pass
            else:
                raise NotNameError(f'неправильный ввод имени')
            if '@' and '.' in e_mail:
                pass
            else:
                raise NotEmailError(f'Неверный ввод мыла')
            if age in range(10, 100):
                pass
            else:
                raise NotAgeError(f'Неверный ввод возраста')
            list_ok.append(line)
        except ValueError:
            list_nok.append(line)
        except NotNameError:
            list_nok.append(line)
        except NotEmailError:
            list_nok.append(line)
        except NotAgeError:
            list_nok.append(line)

with open('registrations_good.txt', 'w', encoding='utf-8') as fle:
    for ln in list_ok:
        fle.write(ln)

with open('registrations_false.txt', 'w', encoding='utf-8') as fil:
    for lin in list_nok:
        fil.write(lin)
