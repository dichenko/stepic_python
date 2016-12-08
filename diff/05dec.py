import hashlib
m = hashlib.md5()
line ="abc"
for i in range(10000000000):
    line1 = line+str(i)
    m.update(line1.encode('utf-8'))
    s = (m.hexdigest())
    if s[:5] == '00000':
        break
print(line1)
print(s)




print (m.hexdigest())
