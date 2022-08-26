import csv
import os
import zipfile
from collections import defaultdict, Counter
from threading import Thread


class UnZip(Thread):

    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name

    def run(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filenames in zfile.namelist():
            zfile.extract(filenames)


class CreateDict(Thread):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count_dict = defaultdict(int)
        self.new_dict = defaultdict(list)
        self.avarage_price_dict = defaultdict(int)
        self.volatility_dict = defaultdict(int)
        self.new_list = []
        self.dictik = defaultdict(int)

    def run(self):
        path = "C:/Users/User/PycharmProjects/pythonProject/svyat777/my works/trades"
        normal_path = os.path.normpath(path)
        for dirpath, dirname, filename in os.walk(normal_path):
            for file in filename:
                full_file_path = dirpath + '\\' + file
                count = 0
                with open(full_file_path, 'r') as fle:
                    for row in csv.reader(fle):
                        if count == 0:
                            pass
                        else:
                            self.new_dict[row[0]].append(row[2])
                            self.count_dict[row[0]] = count
                        count += 1
        counter = 0
        for key, val_price, val_count in zip(self.new_dict.keys(), self.new_dict.values(), self.count_dict.values()):
            key = f'ТИКЕР{counter + 1}'
            average_price = sum(float(i) for i in val_price) / int(val_count)
            min_prise = min(float(m) for m in val_price)
            max_price = max(float(l) for l in val_price)
            self.avarage_price_dict[key] = round(average_price, 2)
            self.volatility_dict[key] = round(((max_price - min_prise) / average_price) * 100, 2)
            counter += 1
        output = Counter(self.volatility_dict)
        output_three_max = output.most_common(3)
        print('Mаксимальная волатильность:')
        for lll in output_three_max:
            print(' ' * 4, f'{lll[0]} - {lll[1]}%')
        for keys, values in self.volatility_dict.items():
            if values == 0:
                self.new_list.append(keys)
            else:
                self.dictik[keys] = values
        output_three_min = sorted(list(self.dictik.items()), key=lambda tup: tup[1])[:3]
        print('Mинимальная волатильность:')
        for it in output_three_min:
            print(' ' * 4, f'{it[0]} - {it[1]}%')
        print('Нулевая волатильность:')
        string = ''
        for op in self.new_list:
            string += op + ',' + ' '
        print(' ' * 4, string[:-2])


a = UnZip(file_name='trades.zip')
b = CreateDict()

# a.start()
b.start()
# a.join()
b.join()
