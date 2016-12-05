class Space(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.vars = []

    def add(self, var):
        self.vars.append(var)

global_ = Space()


n = int(input())
for i in range(n):
    command, foo_name, argu = input().split()
    if command == 'create':
        foo_name = Space(argu)
    elif command == 'add':
        foo_name.add(argu)
    elif command == 'get':
        pass
