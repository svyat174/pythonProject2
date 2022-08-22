import zipfile

txt = 'буква'
txt_2 = 'частота'
txt_3 = ''
txt_4 = 'Итого'


class FindAlphaWord:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char not in self.stat:
                            self.stat[char] = 1
                        else:
                            self.stat[char] += 1
        # print(self.stat)

    def sort_frequency_low(self):
        sorted_values = sorted(self.stat.values(), reverse=True)
        new_stat_dict = {}
        for i in sorted_values:
            for l in self.stat.keys():
                if self.stat[l] == i:
                    new_stat_dict[l] = self.stat[l]
        sum_value = 0
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        print(f'|{txt:^20}|{txt_2:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        for kk, value in new_stat_dict.items():
            sum_value += value
            print(f'|{kk:^20}|{value:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        print(f'|{txt_4:^20}|{sum_value:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')

    def sort_frequency_up(self):
        sorted_values = sorted(self.stat.values())
        new_stat_dict = {}
        for i in sorted_values:
            for l in self.stat.keys():
                if self.stat[l] == i:
                    new_stat_dict[l] = self.stat[l]
        sum_value = 0
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        print(f'|{txt:^20}|{txt_2:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        for kk, value in new_stat_dict.items():
            sum_value += value
            print(f'|{kk:^20}|{value:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        print(f'|{txt_4:^20}|{sum_value:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')

    def sort_alpabit_up(self):
        sum_value = 0
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        print(f'|{txt:^20}|{txt_2:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        for kk, value in sorted(self.stat.items(), reverse=True):
            sum_value += value
            print(f'|{kk:^20}|{value:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        print(f'|{txt_4:^20}|{sum_value:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')

    def sort_alpabit_low(self):
        sum_value = 0
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        print(f'|{txt:^20}|{txt_2:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        for kk, value in sorted(self.stat.items()):
            sum_value += value
            print(f'|{kk:^20}|{value:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')
        print(f'|{txt_4:^20}|{sum_value:^20}|')
        print(f'+{txt_3:-^20}+{txt_3:-^20}+')


a = FindAlphaWord(file_name='voyna-i-mir.txt.zip')
a.unzip()
a.collect()
a.sort_frequency_low()
a.sort_frequency_up()
a.sort_alpabit_up()
a.sort_alpabit_low()
