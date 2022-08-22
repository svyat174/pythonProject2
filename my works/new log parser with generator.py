class LogParser:

    def __init__(self):
        self.new_dict = {}

    def ok_logs(self):
        with open('events.txt', 'r') as file:
            for line in file:
                if line[-4:-1] == ' OK':
                    a = line[0:17] + ']'
                    if a not in self.new_dict:
                        self.new_dict[a] = 1
                    else:
                        self.new_dict[a] += 1

    def nok_logs(self):
        with open('events.txt', 'r') as file:
            for line in file:
                if line[-5:-1] == ' NOK':
                    b = line[0:17] + ']'
                    if b not in self.new_dict:
                        self.new_dict[b] = 1
                    else:
                        self.new_dict[b] += 1

    def generate(self):
        for time, key in self.new_dict.items():
            string_nok = time + ' ' + str(key)
            yield string_nok


gen = LogParser()
gen.nok_logs()
for kk in gen.generate():
    print(kk)
