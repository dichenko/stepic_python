import hashlib
m = hashlib.md5()
line ="abc"

m.update(line.encode('utf-8'))
print (m.hexdigest())
