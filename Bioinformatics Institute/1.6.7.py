def find_path(graph, start, end, path=[]):
    """
    http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml
    :param graph:
    :param start:
    :param end:
    :param path:
    :return:
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def obrabotka(x):
    """
    :param x: строка вида A : B C
    :return: k = A, [B,C]
    """
    t,y = x.split(':')
    t = t[:-1]
    y = y.split()
    return t,y

n = int(input())
cl = []
for i in range(n):
    cl.append(input())


parents = {}
children = {}
for el in cl:
    if ':' not in el:
        parents[el] = []
    else:
        t,y = obrabotka(el)
        parents[t] = y



q = int(input())
ans = []
for i in range(q):
    y,x = input().split()
    if find_path(parents,x,y):
        ans.append('Yes')
    else:
        ans.append('No')

for el in ans:
    print(el)


