def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def obrabotka(x):
    """
    :param x: строка вида A : B C
    :return: k = A, (B,C)
    """
    t,y = x.split(':')
    t = t[:-1]
    y = y.split()
    return t,y
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
    else:
        t,y = obrabotka(el)
        parents[t] = y
print(parents)



