import requests
path = 'https://stepic.org/media/attachments/course67/3.6.3/'
name = '699991.txt'
r = requests.get(path+name)
s = r.text
while 1:
    r = requests.get(path+s)
    s = r.text
    print(s)
