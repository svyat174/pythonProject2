from random import randint
from termcolor import cprint


# Реализовал модель человека.
# Человек может есть, работать, смотреть МТВ, ходить в магазин, покупать корм котам, убираться дома.
# У человека и кота есть степень сытости.
# реализован дом, внутри дома деньги, еда, грязь от котов и еда для котов
# Если сытость < 0 единиц, человек и кот умирает.
# Человеку и котам надо прожить 365 дней.


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def bring_cat(self, cat):
        cat.house = self.house
        cprint('{} подобрал кота {}'.format(self.name, cat.cat_name))

    def clean_after_cat(self):
        cprint('{} убрался дома'.format(self.name), color='cyan')
        self.house.cat_dirty -= 100
        self.fullness -= 20

    def go_to_cat_eat(self):
        cprint('{} купил корм коту'.format(self.name), color='cyan')
        self.house.cat_food += 50
        self.house.money -= 50

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 40:
            self.eat()
        elif self.house.food < 40:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_dirty > 100:
            self.clean_after_cat()
        elif self.house.cat_food < 30:
            self.go_to_cat_eat()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 50
        self.cat_dirty = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, корма для кота осталось {}, Грязи от кота {}'.format(
            self.food, self.money, self.cat_food, self.cat_dirty)


class Cat:
    def __init__(self, cat_name):
        self.cat_name = cat_name
        self.cat_fullness = 50
        self.house = None

    def __str__(self):
        return f'Cat - {self.cat_name}, сытость {self.cat_fullness}'

    def cat_eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.cat_name), color='yellow')
            self.cat_fullness += 10
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды'.format(self.cat_name), color='red')

    def wrong_wallpaper(self):
        cprint('{} дерет обои'.format(self.cat_name), color='magenta')
        self.house.cat_dirty += 10

    def sleep(self):
        cprint('{} спит'.format(self.cat_name), color='grey')
        self.cat_fullness -= 10

    def cat_act(self):
        if self.cat_fullness <= 0:
            cprint('{} умер...'.format(self.cat_name), color='red')
            return
        dice = randint(1, 3)
        if self.cat_fullness < 20:
            self.cat_eat()
        elif dice == 1:
            self.wrong_wallpaper()
        else:
            self.sleep()


citizens = [
    Man(name='Свят'),
    Man(name='Кристина'),
    Man(name='Ваня'),
]

cats = [
    Cat(cat_name='Vasya'),
    Cat(cat_name='Macho'),
    Cat(cat_name='Teddy')
]

my_sweet_home = House()

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
for citisen, cat in zip(citizens, cats):
    citisen.bring_cat(cat)

for day in range(1, 365):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    for cat in cats:
        cat.cat_act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    for cat in cats:
        print(cat)
    print(my_sweet_home)

# Создали трех людей, живущих в одном доме - Свята, Кристину и Ваню
# Создали класс Дом, в нем должно быть холодильник с едой и тумбочка с деньгами, корм коту и метелка для уборки
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке, метла в чулане и корм в тумбочке.
