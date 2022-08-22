class LogParser:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_name_ok_m = 'OK_min.txt'
        self.file_name_ok_h = 'OK_hour.txt'
        self.file_name_ok_d = 'OK_day.txt'
        self.file_name_nok_m = 'NOK_min.txt'
        self.file_name_nok_h = 'NOK_hour.txt'
        self.file_name_nok_d = 'NOK_day.txt'
        self.file_name_nok_count_min = 'new_count_file_min.txt'
        self.file_name_nok_count_hour = 'new_count_file_hour.txt'
        self.file_name_nok_count_days = 'new_count_file_days.txt'
        self.new_dict_min = {}
        self.new_dict_hour = {}
        self.new_dict_day = {}

    def count_in_one_minutes(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if line[-4:-1] == ' OK':
                    a = line[0:17] + ']' + line[-4:-1]
                    with open(self.file_name_ok_m, 'a+') as file1:
                        file1.write(a + "\n")
                else:
                    b = line[0:17] + ']' + line[-5:-1]
                    with open(self.file_name_nok_m, 'a+') as file1:
                        file1.write(b + "\n")
        with open(self.file_name_nok_m, 'r') as fillle:
            for lines in fillle:
                if lines not in self.new_dict_min:
                    self.new_dict_min[lines] = 1
                else:
                    self.new_dict_min[lines] += 1
        for date, count in self.new_dict_min.items():
            with open(self.file_name_nok_count_min, 'a') as fl:
                fl.write(date[:-4] + str(count) + '\n')

    def count_in_one_hours(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if line[-4:-1] == ' OK':
                    a = line[0:14] + ']' + line[-4:-1]
                    with open(self.file_name_ok_h, 'a+') as file1:
                        file1.write(a + "\n")
                else:
                    b = line[0:14] + ']' + line[-5:-1]
                    with open(self.file_name_nok_h, 'a+') as file1:
                        file1.write(b + "\n")
        with open(self.file_name_nok_h, 'r') as fillle:
            for lines in fillle:
                if lines not in self.new_dict_hour:
                    self.new_dict_hour[lines] = 1
                else:
                    self.new_dict_hour[lines] += 1
        for date, count in self.new_dict_hour.items():
            with open(self.file_name_nok_count_hour, 'a+') as fl:
                fl.write(date[:-4] + str(count) + '\n')

    def count_in_one_days(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if line[-4:-1] == ' OK':
                    a = line[0:11] + ']' + line[-4:-1]
                    with open(self.file_name_ok_d, 'a+') as file1:
                        file1.write(a + "\n")
                else:
                    b = line[0:11] + ']' + line[-5:-1]
                    with open(self.file_name_nok_d, 'a+') as file1:
                        file1.write(b + "\n")
        with open(self.file_name_nok_d, 'r') as fillle:
            for lines in fillle:
                if lines not in self.new_dict_day:
                    self.new_dict_day[lines] = 1
                else:
                    self.new_dict_day[lines] += 1
        for date, count in self.new_dict_day.items():
            with open(self.file_name_nok_count_days, 'a+') as fl:
                fl.write(date[:-4] + str(count) + '\n')


d = LogParser(file_name='events_.txt')
d.count_in_one_minutes()
d.count_in_one_hours()
d.count_in_one_days()
