n = int(input())
raw_data = []
for i in range(n):
    d = input().split(';')
    d[1] = int(d[1])
    d[3] = int(d[3])
    raw_data.append(d)

komands = {}
for st in raw_data:
    if st[0] not in komands:
        komands[st[0]] = [1]
    else:
        komands[st[0]][0] +=1
    if st[2] not in komands:
        komands[st[2]] = [1]
    else:
        komands[st[2]][0] +=1
for komanda in komands:
    komands[komanda] += [0,0,0]
for st in raw_data:
    if st[1] == st[3]:
        komands[st[0]][2] += 1
        komands[st[2]][2] += 1
    elif st[1] > st[3]:
        komands[st[0]][1] += 1
        komands[st[2]][3] += 1
    else:
        komands[st[0]][3] += 1
        komands[st[2]][1] += 1

for kom in komands:
    x = komands[kom]
    x.append(x[1]*3+x[2])


for kom in komands:
    x = komands[kom]
    print(kom,':', sep = '', end = '')
    print(*x)


