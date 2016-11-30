n = int(input())
x = 0
y = 0
for i in range(n):
    s = input().split()
    s[1] = int(s[1])
    if s[0] == 'восток':
        x = x + s[1]
    elif s[0] == 'запад':
        x = x - s[1]
    elif s[0] == 'север':
        y = y + s[1]
    else:
        y = y - s[1]
print(x,y)

