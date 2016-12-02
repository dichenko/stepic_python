with open('data.txt') as f:
    s = f.readlines()

for i in range(len(s)):
    s[i] = s[i].split()

for i in range(len(s)):
        s[i][0] = int(s[i][0])
        s[i][2] = float(s[i][2])

clas = {}

for el in s:
    if el[0] in clas:
        clas[el[0]][0] += 1
        clas[el[0]][1] += el[2]
    else:
        clas[el[0]] = [1,el[2]]


for el in clas:
    clas[el].append(clas[el][1]/clas[el][0])

for i in range(1,12):
    if i in clas:
        print(i,clas[i][2])
    else:
        print(i,': -')


print(clas)




