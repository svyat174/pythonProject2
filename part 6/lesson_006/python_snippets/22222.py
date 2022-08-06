a = "the_stealth_warrior"
n = '_-'
word = ''
list_1 = []
cc = ''
for i in a:
    if i in n:
        word += ' '
    else:
        word += i
print(word)
aa = word.split()
for i in aa:
    if i == aa[0]:
        cc += i
    else:
        cc += i.title()
print(cc)
