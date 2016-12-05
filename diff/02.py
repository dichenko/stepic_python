#http://adventofcode.com/2016/day/2
with open('input.txt') as f:
    data = f.readlines()




a = [[0,   0, '1', 0,  0],
     [0,  '2','3','4', 0],
     ['5','6','7','8','9'],
     [0   'A','B','C', 0],
     [0,  0,  'D',  0, 0]
     ]

current_poss = [2, 0] #5
cP = current_poss
current_code = ''



def move(s):
    global cP
    #print(s, end=' ')
    if s == 'U':
        if  cP[0] > 0 and a[cP[0]-1] != 0:
            cP[0] -= 1
            #print(current_poss[0] + 1, current_poss[1] + 1)
    elif s == 'D':
        if cP[0] < 4 and  a[cP[0] + 1] != 0  :
            cP[0] += 1
            #print(current_poss[0] + 1, current_poss[1] + 1)
    elif s == 'L':
        if cP[1] > 0 and a[cP[1] - 1] != 0  :
            cP[1] -= 1
            #print(current_poss[0] + 1, current_poss[1] + 1)
    elif s == 'R':
        if cP[1] < 4 and  a[cP[1] + 1] != 0  :
            cP[1] += 1
            #print(current_poss[0] + 1, current_poss[1] + 1)


for el in data:
    #print('new string', el)
    for com in el:
        #print('\t','new bukva', com)
        move(com)
    current_code += str(a[current_poss[0]][current_poss[1]])
    #print(current_poss[0] + 1, current_poss[1]+1)

print(current_code)




