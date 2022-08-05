# 'task where return remove 5-dig string, but else is still'
sentence = input('enter you text')

a = []
b = ''
n = 0
for i in sentence.split():
    if len(i) > 4:
        a.append(i[::-1])
    if len(i) <= 4:
        a.append(i)
for kk in a:
    n += 1
    if len(a) > n:
        b += kk + ' '
    if len(a) == n:
        b += kk
print(b)