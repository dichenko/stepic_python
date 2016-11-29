def obrabotka(x):
    """
    :param x: строка вида A : B C
    :return: k = A, (B,C)
    """
    t,y = x.split(':')
n = int(input())
cl = []
for i in range(n):
    cl.append(input())

q = int(input())
qw = []
for i in range(q):
    qw.append(input())
parents = {}
children = {}
for el in cl:
    if len(el) == 1:
        parents[el] = 0
    else


