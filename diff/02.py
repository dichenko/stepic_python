#http://adventofcode.com/2016/day/2

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

current_poss = [1, 1] #5
cP = current_poss


def move(s):
    global cP
    if s == 'U':
        if cP[1] > 0:
            cP[1] -= 1
    elif s == 'D':
        if cP[1] < 2:
            cP[1] += 1
    elif s == 'L':
        if cP[0] > 0:
            cP[0] -= 1


