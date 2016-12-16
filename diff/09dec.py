with open('input91.txt') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i][:-1]

dat = ''
for el in data:
    dat += el


counter = 0

print(dat)


def index_of_skob():
    # Возвращает индекс ближайшей закрывающей скобки
    global dat
    return dat.find(')')


def parsing_of_skobka(x):
    """
    Принимает строку вида (3х5) и возвращает два целых числа
    :param x:
    :return:
    """
    f = (x[1:-1].split('x'))
    a, b = f[0], f[1]
    return a, b


def run_parse():
    global dat
    t = dat[:index_of_skob()+1 ]  # смотрим на скобку-маркер
    l, n = parsing_of_skobka(t)  # Парсим параметры L и N
    dat = dat[index_of_skob()+1:]  # Отрезаем маркер от строки
    print(l,'____', n,'____', dat)


run_parse()

#######__________main_cycle___#########################
# while len(dat) > 0:
#    if dat[0] == ('('):
#        run_parse()
#    else:
#        counter += 1
#        dat = dat[1:]
