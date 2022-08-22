import os
import shutil
import time

path = 'D:/icons'
new_path = 'D:/icons_by_year'
normal_path = os.path.normpath(path)
normal_path_1 = os.path.normpath(new_path)
new_dict = {}
for dirpath, dirname, filename in os.walk(normal_path):
    for file in filename:
        full_file_path = dirpath + '\\' + file
        secs = os.path.getmtime(full_file_path)
        file_time = time.gmtime(secs)
        if file_time[0] not in new_dict:
            new_dict[file_time[0]] = {file_time[1]}
        else:
            new_dict[file_time[0]].add(file_time[1])
for key, values in new_dict.items():
    print(key)
    os.makedirs(normal_path_1 + '\\' + str(key))
    for mnth in values:
        os.makedirs(normal_path_1 + '\\' + str(key) + '\\' + str(mnth))
for dirpath, dirname, filename in os.walk(normal_path):
    for file in filename:
        full_file_path = dirpath + '\\' + file
        secs = os.path.getmtime(full_file_path)
        file_time = time.gmtime(secs)
        shutil.copy2(full_file_path, f'{normal_path_1}\\{file_time[0]}\\{file_time[1]}')
