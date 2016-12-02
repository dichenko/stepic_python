n = int(input())
dict = []
for i in range(n):
    dict.append(input().lower())
s = []
n = int(input())
for i in range(n):
    s+=( input().lower().split())
s = list(set(s))


for el in s:
    if el not in dict:
        print(el)

