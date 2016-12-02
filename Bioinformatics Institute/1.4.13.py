namespaces = {'global': None} # ключ - namespace. значение - parent
variables = {'global': set()} # ключ - namespace. значение - множество переменных

def create(name, parent):
    namespaces[name] = parent

def addd(name, var_name):
    if name in variables:
        variables[name].add(var_name)
    else:
        variables[name] = {var_name}


