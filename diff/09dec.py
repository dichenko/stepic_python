with open('input9.txt') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i][:-1]

dat = ''
for el in data:
    dat += el

print(dat)
counter = 1



