data = open('xxx.txt', 'r', encoding='utf-16').read()

ss = ''
for x in data:
    if ord(x)> 128:
        continue
    ss += x


print(ss)