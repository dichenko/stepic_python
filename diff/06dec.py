
with open('input6.txt') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i][:-1]

strings = ['0']*len(data)

for i in range(len(data)):
    s = []
    for k in range(len(data[i])):
        s.append(data[i][k])
    strings[i] = s.copy()

print(strings)














