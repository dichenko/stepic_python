namespaces = {'global': None} # ключ - namespace. значение - parent
variables = {'global': set()} # ключ - namespace. значение - множество переменных

def create(name, parent):
    namespaces[name] = parent


def addd(name, var_name):
    if name in variables:
        variables[name].add(var_name)
    else:
        variables[name] = {var_name}


def get(foo_name, var_name):
    while foo_name != 'global':
        if var_name in variables[foo_name]:
            print(foo_name)
            break
        else: foo_name = namespaces[foo_name]
    if foo_name == 'global':
        if var_name in variables[foo_name]:
             print(foo_name)
        else:
             print('None')


n = int(input())

for i in range(n):
    command, foo_name, argu = input().split()
    if command == 'create':
        create(foo_name, argu)
    elif command == 'add':
        addd(foo_name, argu)
    elif command == 'get':
        get(foo_name, argu)


