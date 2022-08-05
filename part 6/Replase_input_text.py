text = input('Enter your text: ')
a = []
len_a = []
b = ''
n = 0
for i in text.split():
    a.append('* ' + i[::-1])
    len_a.append(len(a[n]))
    n += 1
for kk in a:
    b += kk + (max(len_a) - len(kk) + 1) * ' ' + '*' + '\n'
b = '*' * (max(len_a) + 2) + '\n' + b + '*' * (max(len_a) + 2)
print(b)
