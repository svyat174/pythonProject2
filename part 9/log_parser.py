class LogParser:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_name_ok = 'OK.txt'
        self.file_name_nok = 'NOK.txt'
        self.file_name_nok_count = 'new_count_file'

    def sorted_to_two_files(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if line[-4:-1] == ' OK':
                    a = '[' + line[1:17] + ']' + line[-4:-1]
                    with open(self.file_name_ok, 'a') as file1:
                        file1.write(a + "\n")
                else:
                    b = '[' + line[1:17] + ']' + line[-5:-1]
                    with open(self.file_name_nok, 'a') as file1:
                        file1.write(b + "\n")

    def count_in_one_minutes(self):
        new_dict = {}
        with open(self.file_name_nok, 'r') as fillle:
            for line in fillle:
                if line not in new_dict:
                    new_dict[line] = 1
                else:
                    new_dict[line] += 1
        for date, count in new_dict.items():
            with open(self.file_name_nok_count, 'a') as fl:
                fl.write(date[:-4] + str(count) + '\n')


d = LogParser(file_name='events.txt')
d.sorted_to_two_files()
d.count_in_one_minutes()
