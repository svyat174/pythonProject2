#по-приколу

w = input('Введите предложение на английском: ')
dict_1 = {}
dict_2 = {}
eng_word = 'abcdefghijklmnopqrstuvwxyz'
n = 0
s = []
ss = []
z = 0
for i in eng_word:
    n += 1
    dict_1[i] = n
for kk in w.split():
    s.append(kk)
    dict_2[kk] = 0
    d = 0
    for l in kk:
        d += dict_1[l]
        dict_2[kk] = d
for key in dict_2:
    ss.append(dict_2[key])


print(max(dict_2, key=dict_2.get))
